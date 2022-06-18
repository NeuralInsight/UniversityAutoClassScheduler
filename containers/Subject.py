from PyQt5 import QtWidgets, QtGui, QtCore
from components import Database as db
from py_ui import Subject as Parent
import json
import os 

icon_path = os.path.join(os.getcwd(), 'assets/icons')


class Subject:
    def __init__(self, id):
        self.id = id
        # New instance of dialog
        self.dialog = dialog = QtWidgets.QDialog()
        # Initialize custom dialog
        self.parent = parent = Parent.Ui_Dialog()
        # Add parent to custom dialog
        parent.setupUi(dialog)
        parent.radioLec.setChecked(True)
        #parent.radioYes.setChecked(True)
        if id:
            self.fillForm()
        self.setupInstructors()
        parent.btnFinish.clicked.connect(self.finish)
        parent.btnCancel.clicked.connect(self.dialog.close)
        parent.txtSelectIns.textChanged.connect(lambda value: self.onSearchTextChanged(value))

        dialog.exec_()


    def fillForm(self):
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT name, hours, code, description, type FROM subjects WHERE id = ?', [self.id])
        result = cursor.fetchone()
        conn.close()
        self.parent.lineEditName.setText(str(result[0]))
        self.parent.lineEditHours.setText(str(result[1]))
        self.parent.lineEditCode.setText(str(result[2]))
        self.parent.lineEditDescription.setText(str(result[3]))
        if result[4] == 'lec':
            self.parent.radioLec.setChecked(True)
        elif result[4] == 'lab':
            self.parent.radioLab.setChecked(True)
        else:
            self.parent.radioAny.setChecked(True)

    def setupInstructors(self):
        self.tree = tree = self.parent.treeSchedule
        self.model = model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'Available', 'Name'])
        self.proxyModel = proxyModel = SortFilterProxyModel(
            tree, recursiveFilteringEnabled=True
        )
        self.proxyModel.setSourceModel(model)
        tree.setModel(proxyModel)
        tree.setColumnHidden(0, True)
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM instructors WHERE active = 1')
        instructors = cursor.fetchall()
        subjectAssignments = []
        if self.id:
            cursor.execute('SELECT instructors FROM subjects WHERE id = ?', [self.id])
            subjectAssignments = list(map(lambda id: int(id), json.loads(cursor.fetchone()[0])))
        conn.close()
        for entry in instructors:
            id = QtGui.QStandardItem(str(entry[0]))
            id.setEditable(False)
            availability = QtGui.QStandardItem()
            availability.setCheckable(True)
            availability.setCheckState(2 if entry[0] in subjectAssignments else 0)
            availability.setEditable(False)
            name = QtGui.QStandardItem(str(entry[1]))
            name.setEditable(False)
            model.appendRow([id, availability, name])

    def finish(self):
        if not self.parent.lineEditName.text():
            return False
        if not self.parent.lineEditCode.text():
            return False
        if not self.parent.lineEditHours.text() or float(self.parent.lineEditHours.text()) < 0 or float(
                self.parent.lineEditHours.text()) > 12 or not (
                float(self.parent.lineEditHours.text()) / .5).is_integer():
            return False
        instructors = []
        for row in range(0, self.model.rowCount()):
            if self.model.item(row, 1).checkState() == 0:
                continue
            instructors.append(self.model.item(row, 0).text())
        name = self.parent.lineEditName.text()
        code = self.parent.lineEditCode.text()
        hours = self.parent.lineEditHours.text()
        description = self.parent.lineEditDescription.text()
        if self.parent.radioLec.isChecked():
            type = 'lec'
        elif self.parent.radioLab.isChecked():
            type = 'lab'
        else:
            type = 'any'
        data = [name, hours, code, description, json.dumps(instructors), type, self.id]
        if not self.id:
            data.pop()
        self.insertSubject(data)
        self.dialog.close()

    def onSearchTextChanged(self, text):
        self.proxyModel.setFilterByColumn(text,2)

    @staticmethod
    def insertSubject(data):
        conn = db.getConnection()
        cursor = conn.cursor()
        if len(data) > 6:
            cursor.execute(
                'UPDATE subjects SET name = ?, hours = ?, code = ?, description = ?, instructors = ?, type = ? WHERE id = ?',
                data)
        else:
            cursor.execute(
                'INSERT INTO subjects (name, hours, code, description, instructors, type) VALUES (?, ?, ?, ?, ?, ?)',
                data)
        conn.commit()
        conn.close()


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QtCore.QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.filters = {}

    def setFilterByColumn(self, regex, column):
        self.filters[column] = regex
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        for key, regex in self.filters.items():
            ix = self.sourceModel().index(source_row, key, source_parent)
            if ix.isValid():
                text = self.sourceModel().data(ix)
                if not regex in text:
                    return False
        return True

class Tree:
    def __init__(self, tree):
        self.tree = tree
        self.model = model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'کد درس', 'نام درس', 'نوع درس', 'اساتید', 'عملیات'])
        self.proxyModel = proxyModel = SortFilterProxyModel(
            tree, recursiveFilteringEnabled=True
        )
        self.proxyModel.setSourceModel(self.model)
        tree.setModel(proxyModel)
        tree.setColumnHidden(0, True)
        tree.header().setDefaultAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.display()

    def display(self):
        self.model.removeRows(0, self.model.rowCount())
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, code, name, type, instructors FROM subjects')
        result = cursor.fetchall()
        cursor.execute('SELECT id, name FROM instructors WHERE active = 1')
        instructorList = dict(cursor.fetchall())
        conn.close()
        for entry in result:
            id = QtGui.QStandardItem(str(entry[0]))
            id.setEditable(False)
            code = QtGui.QStandardItem(entry[1])
            code.setEditable(False)
            name = QtGui.QStandardItem(entry[2])
            name.setEditable(False)
            type = QtGui.QStandardItem(entry[3].upper())
            type.setEditable(False)
            instructorID = list(
                set(map(lambda id: int(id), json.loads(entry[4]))).intersection(set(instructorList.keys())))
            if len(instructorID) > 3:
                instructorText = ', '.join(list(map(lambda id: instructorList[id], instructorID[0:3]))) + ' and ' + str(
                    len(instructorID) - 3) + ' more'
            elif len(instructorID) > 0:
                instructorText = ', '.join(list(map(lambda id: instructorList[id], instructorID)))
            else:
                instructorText = ''
            instructors = QtGui.QStandardItem(instructorText)
            instructors.setEditable(False)
            edit = QtGui.QStandardItem()
            edit.setEditable(False)
            self.model.appendRow([id, code, name, type, instructors, edit])
            # Edit buttons
            frameEdit = QtWidgets.QFrame()
            btnEdit = QtWidgets.QPushButton('', frameEdit)
            btnEdit.setObjectName("btnEdit")
            btnEdit.setFlat(True)
            btnEdit.setIcon(QtGui.QIcon(os.path.join(icon_path, 'icons8-edit-64.png')))
            btnEdit.setIconSize(QtCore.QSize(32, 32))
            btnEdit.setFixedSize(QtCore.QSize(50, 32))
            btnEdit.clicked.connect(lambda state, id=entry[0]: self.edit(id))
            # Delete buttons
            btnDelete = QtWidgets.QPushButton('', frameEdit)
            btnDelete.setObjectName("btnDelete")
            btnDelete.setFlat(True)
            btnDelete.setIcon(QtGui.QIcon(os.path.join(icon_path, 'icons8-delete-64.png')))
            btnDelete.setIconSize(QtCore.QSize(32, 32))
            btnDelete.setFixedSize(QtCore.QSize(50, 32))
            btnDelete.clicked.connect(lambda state, id=entry[0]: self.delete(id))
            
            frameLayout = QtWidgets.QHBoxLayout(frameEdit)
            frameLayout.setContentsMargins(0, 0, 0, 0)
            frameLayout.addWidget(btnEdit)
            frameLayout.addWidget(btnDelete)
            # Append the widget group to edit item
            self.tree.setIndexWidget(self.proxyModel.mapFromSource(edit.index()), frameEdit)
        
        self.tree.setSortingEnabled(True)
        self.tree.setColumnWidth(4, 280)
        self.tree.resizeColumnToContents(2)

    def onSearchTextChanged(self, text):
        self.proxyModel.setFilterByColumn(text,2)
        self.display()

    def edit(self, id):
        Subject(id)
        self.display()

    def delete(self, id):
        confirm = QtWidgets.QMessageBox()
        confirm.setIcon(QtWidgets.QMessageBox.Warning)
        confirm.setText('Are you sure you want to delete this entry?')
        confirm.setWindowTitle('Confirm Delete')
        confirm.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        result = confirm.exec_()
        if result == 16384:
            conn = db.getConnection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM subjects WHERE id = ?', [id])
            conn.commit()
            conn.close()
            self.display()
