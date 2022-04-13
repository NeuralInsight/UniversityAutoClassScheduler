from PyQt5 import QtWidgets, QtGui
from qt_ui.v1 import Share as Parent
from components import Database as db
import json

class Share:
    def __init__(self, subject_id, section_id):
        self.id = int(subject_id)
        self.section_id = int(section_id)
        self.shareId = False
        self.shareMembersText = False
        # New instance of dialog
        self.dialog = dialog = QtWidgets.QDialog()
        # Initialize custom dialog
        self.parent = parent = Parent.Ui_Dialog()
        # Add parent to custom dialog
        parent.setupUi(dialog)
        self.setSharings()
        parent.btnFinish.clicked.connect(self.finish)
        parent.btnCancel.clicked.connect(self.dialog.close)
        dialog.exec_()

    def getShareData(self):
        return tuple([self.shareId, self.shareMembersText])

    def setSharings(self):
        self.tree = tree = self.parent.treeSections
        self.model = model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['شناسه', 'گروه', 'شناسه گروه'])
        tree.setModel(model)
        tree.setColumnHidden(0, True)
        tree.setColumnHidden(2, True)
        model.itemChanged.connect(lambda item: self.toggleSharing(item))
        conn = db.getConnection()
        cursor = conn.cursor()
        # Get sections with mutual subjects
        if self.section_id:
            cursor.execute('SELECT id, name, subjects FROM sections WHERE active = 1 AND id != ?', [self.section_id])
        else:
            cursor.execute('SELECT id, name, subjects FROM sections WHERE active = 1')
        sections = cursor.fetchall()
        conn.close()
        for section in sections:
            if self.id not in list(map(lambda id: int(id), json.loads(section[2]))):
                continue
            id = QtGui.QStandardItem()
            id.setEditable(False)
            sectionList = QtGui.QStandardItem(section[1])
            sectionList.setEditable(False)
            sectionID = QtGui.QStandardItem(str(section[0]))
            sectionID.setEditable(False)
            self.model.appendRow([id, sectionList, sectionID])
        # TODO: Get existing sharings

    def finish(self):
        if not self.tree.selectedIndexes():
            return False
        shareId = self.model.item(self.tree.selectedIndexes()[0].row()).text()
        shareId = False if not shareId else shareId
        conn = db.getConnection()
        cursor = conn.cursor()
        if not shareId:
            cursor.execute('INSERT INTO sharings (subjectId, sections) VALUES (?, ?)', [self.id, json.dumps([self.section_id, self.model.item(self.tree.selectedIndexes()[0].row(), 2).text()])])
            self.shareId = cursor.lastrowid
        conn.commit()
        conn.close()
        self.shareMembersText = self.model.item(self.tree.selectedIndexes()[0].row(), 1).text()
        self.dialog.close()