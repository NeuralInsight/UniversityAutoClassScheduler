from PyQt5 import QtWidgets, QtGui, QtCore
from components import Database as db, Timetable
from py_ui import Room as Parent
import json
import os
import qtawesome as qta



class Room:
    def __init__(self, id):
        self.id = id
        # New instance of dialog
        self.dialog = dialog = QtWidgets.QDialog()
        # Initialize custom dialog
        self.parent = parent = Parent.Ui_Dialog()
        # Add parent to custom dialog
        parent.setupUi(dialog)
        # Connect timetable widget with custom timetable model
        if id:
            self.fillForm()
        else:
            self.table = Timetable.Timetable(parent.tableSchedule)
        parent.btnFinish.clicked.connect(self.finish)
        parent.btnCancel.clicked.connect(self.dialog.close)
        dialog.exec_()

    def fillForm(self):
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT name, schedule, type FROM rooms WHERE id = ?', [self.id])
        result = cursor.fetchone()
        conn.close()
        self.parent.lineEditName.setText(str(result[0]))
        self.table = Timetable.Timetable(self.parent.tableSchedule, json.loads(result[1]))
        if result[2] == 'lec':
            self.parent.radioLec.setChecked(True)
        else:
            self.parent.radioLab.setChecked(True)

    def finish(self):
        if not self.parent.lineEditName.text():
            self.error('لطفا نام کلاس را وارد کنید!')
            return False
        name = self.parent.lineEditName.text()
        type = 'lec' if self.parent.radioLec.isChecked() else 'lab'
        data = [name, json.dumps(self.table.getData()), type, self.id]
        if not self.id:
            data.pop()
        self.insertRoom(data)
        self.dialog.close()

    def error(self, message):
        confirm = QtWidgets.QMessageBox()
        confirm.setIcon(QtWidgets.QMessageBox.Warning)
        confirm.setText(message)
        confirm.setWindowTitle('خطا')
        confirm.setStandardButtons(QtWidgets.QMessageBox.Ok)
        confirm.exec_()

    @staticmethod
    def insertRoom(data):
        conn = db.getConnection()
        cursor = conn.cursor()
        if len(data) > 3:
            cursor.execute('UPDATE rooms SET name = ?, schedule = ?, type = ? WHERE id = ?', data)
        else:
            cursor.execute('INSERT INTO rooms (name, schedule, type) VALUES (?, ?, ?)', data)
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
        model.setHorizontalHeaderLabels(['ID', 'فعال', 'کد کلاس', 'عملیات'])
        self.proxyModel = proxyModel = SortFilterProxyModel(
            tree, recursiveFilteringEnabled=True
        )
        self.proxyModel.setSourceModel(self.model)
        tree.setModel(proxyModel)
        tree.setColumnHidden(0, True)
        tree.header().setDefaultAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        model.itemChanged.connect(lambda item: self.toggleAvailability(item))
        self.display()

    def toggleAvailability(self, item):
        id = self.model.data(self.model.index(item.row(), 0))
        newValue = 1 if item.checkState() == 2 else 0
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('UPDATE rooms SET active = ?  WHERE id = ?', [newValue, id])
        conn.commit()
        conn.close()

    def display(self):
        btnEditIcon = qta.icon('fa.edit', color='#EC7440',color_active='#E25417')
        deletEditIcon = qta.icon('mdi.delete', color='#EC7440',color_active='#E25417')
        self.model.removeRows(0, self.model.rowCount())
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, active, name FROM rooms')
        result = cursor.fetchall()
        conn.close()
        for entry in result:
            id = QtGui.QStandardItem(str(entry[0]))
            id.setEditable(False)
            availability = QtGui.QStandardItem()
            availability.setCheckable(True)
            availability.setCheckState(2 if entry[1] == 1 else 0)
            availability.setEditable(False)
            name = QtGui.QStandardItem(entry[2])
            name.setEditable(False)
            edit = QtGui.QStandardItem()
            edit.setEditable(False)
            self.model.appendRow([id, availability, name, edit])
            # Edit buttons
            frameEdit = QtWidgets.QFrame()
            btnEdit = QtWidgets.QPushButton(btnEditIcon,'')
            btnEdit.setObjectName("btnEdit")
            btnEdit.setFlat(True)
            btnEdit.setIconSize(QtCore.QSize(32, 32))
            btnEdit.setFixedSize(QtCore.QSize(50, 32))
            btnEdit.clicked.connect(lambda state, id=entry[0]: self.edit(id))
            # Delete buttons
            btnDelete = QtWidgets.QPushButton(deletEditIcon,'')
            btnDelete.setObjectName("btnDelete")
            btnDelete.setFlat(True)
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
        self.tree.setColumnWidth(2, 500)
        self.tree.setAlternatingRowColors(True)

    def onSearchTextChanged(self, text):
        self.proxyModel.setFilterByColumn(text,2)
        self.display()

    def edit(self, id):
        Room(id)
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
            cursor.execute('DELETE FROM rooms WHERE id = ?', [id])
            conn.commit()
            conn.close()
            self.display()
