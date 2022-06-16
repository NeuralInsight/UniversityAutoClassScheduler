from PyQt5 import QtWidgets, QtGui, QtCore
from components import Database as db, Timetable
from py_ui import Instructor as Parent
import json


class Instructor:
    def __init__(self, id):
        self.id = id
        self.dialog = dialog = QtWidgets.QDialog()
        # From the qt_ui generated UI
        self.parent = parent = Parent.Ui_Dialog()
        parent.setupUi(dialog)
        if id:
            self.fillForm()
        else:
            # Create a new instance of timetable
            self.table = Timetable.Timetable(parent.tableSchedule)
        parent.btnFinish.clicked.connect(self.finish)
        parent.btnCancel.clicked.connect(self.dialog.close)
        dialog.exec_()

    def fillForm(self):
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT name, hours, schedule FROM instructors WHERE id = ?', [self.id])
        result = cursor.fetchone()
        conn.close()
        self.parent.lineEditName.setText(str(result[0]))
        self.parent.lineEditHours.setText(str(result[1]))
        # Generate timetable from custom schedule
        self.table = Timetable.Timetable(self.parent.tableSchedule, json.loads(result[2]))

    def finish(self):
        # Verification of input
        if not self.parent.lineEditName.text():
            return False
        name = self.parent.lineEditName.text()
        try:
            hours = int(self.parent.lineEditHours.text())
            if hours <= 0 or hours > 100 or hours % .5 != 0:
                return False
        except:
            return False
        data = [name, hours, json.dumps(self.table.getData()), self.id]
        if not self.id:
            data.pop()
        self.insertInstructor(data)
        self.dialog.close()

    @staticmethod
    def insertInstructor(data):
        conn = db.getConnection()
        cursor = conn.cursor()
        if len(data) > 3:
            cursor.execute('UPDATE instructors SET name = ?, hours = ?, schedule = ? WHERE id = ?', data)
        else:
            cursor.execute('INSERT INTO instructors (name, hours, schedule) VALUES (?, ?, ?)', data)
        conn.commit()
        conn.close()
        return True

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
        model.setHorizontalHeaderLabels(['ID', 'Available', 'Name', 'Hours', 'Operation'])
        self.proxyModel = proxyModel = SortFilterProxyModel(
            tree, recursiveFilteringEnabled=True
        )
        self.proxyModel.setSourceModel(self.model)
        tree.setModel(proxyModel)
        tree.setColumnHidden(0, True)
        model.itemChanged.connect(lambda item: self.toggleAvailability(item))
        self.display()

    def toggleAvailability(self, item):
        # Get ID of toggled instructor
        id = self.model.data(self.model.index(item.row(), 0))
        newValue = 1 if item.checkState() == 2 else 0
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('UPDATE instructors SET active = ?  WHERE id = ?', [newValue, id])
        conn.commit()
        conn.close()

    def display(self):
        # Clear model
        self.model.removeRows(0, self.model.rowCount())
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, active, hours, name FROM instructors')
        result = cursor.fetchall()
        conn.close()
        for instr in result:
            # ID Item
            id = QtGui.QStandardItem(str(instr[0]))
            id.setEditable(False)
            # Availability Item
            availability = QtGui.QStandardItem()
            availability.setCheckable(True)
            availability.setCheckState(2 if instr[1] == 1 else 0)
            availability.setEditable(False)
            # Hours Item
            hours = QtGui.QStandardItem(str(instr[2]))
            hours.setEditable(False)
            # Name Item
            name = QtGui.QStandardItem(instr[3])
            name.setEditable(False)
            # Edit Item / Container for operation buttons
            edit = QtGui.QStandardItem()
            edit.setEditable(False)
            # Append items to model
            self.model.appendRow([id, availability, name, hours, edit])
            # Create a widget group for edit and delete buttons
            frameEdit = QtWidgets.QFrame()
            btnEdit = QtWidgets.QPushButton('Edit', frameEdit)
            btnEdit.clicked.connect(lambda state, id=instr[0]: self.edit(id))
            btnDelete = QtWidgets.QPushButton('Delete', frameEdit)
            btnDelete.clicked.connect(lambda state, id=instr[0]: self.delete(id))
            frameLayout = QtWidgets.QHBoxLayout(frameEdit)
            frameLayout.setContentsMargins(0, 0, 0, 0)
            frameLayout.addWidget(btnEdit)
            frameLayout.addWidget(btnDelete)
            # Append the widget group to edit item
            self.tree.setIndexWidget(edit.index(), frameEdit)
            self.tree.setSortingEnabled(True)
            
        self.tree.resizeColumnToContents(2)

    def onSearchTextChanged(self, text):
        self.proxyModel.setFilterByColumn(text,2)

    def edit(self, id):
        Instructor(id)
        self.display()

    def delete(self, id):
        # Show confirm model
        confirm = QtWidgets.QMessageBox()
        confirm.setIcon(QtWidgets.QMessageBox.Warning)
        confirm.setText('Are you sure you want to delete this entry?')
        confirm.setWindowTitle('Confirm Delete')
        confirm.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        result = confirm.exec_()
        # 16384 == Confirm
        if result == 16384:
            conn = db.getConnection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM instructors WHERE id = ?', [id])
            conn.commit()
            conn.close()
            self.display()
