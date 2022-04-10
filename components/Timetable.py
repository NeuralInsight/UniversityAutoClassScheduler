from PyQt5 import QtCore, QtWidgets, QtGui
from components import Settings
from components import TableModel
import json

# Used for displaying toggable timetable
# TODO: Assess for possible different version of timetable widget
class Timetable:
    def __init__(self, table, data = False):
        self.table = table
        header = [['شنبه', 'یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنجشنبه']]
        with open('timeslots.json') as json_file:
            timeslots = json.load(json_file)['timeslots']
        settings = Settings.getSettings()
        header.append(timeslots[settings['starting_time']:settings['ending_time'] + 1])
        self.data = data
        if not data:
            self.data = []
            for i in range(settings['ending_time'] + 1 - settings['starting_time']):
                self.data.append(['در دسترس', 'در دسترس', 'در دسترس', 'در دسترس', 'در دسترس', 'در دسترس'])
        self.model = TimetableModel(header, self.data)
        table.setModel(self.model)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        table.clicked.connect(self.toggleCells)
        table.horizontalHeader().sectionClicked.connect(self.toggleCells)
        table.verticalHeader().sectionClicked.connect(self.toggleCells)
        table.findChild(QtWidgets.QAbstractButton).clicked.connect(self.toggleCells)

    # Toggles the availability and changes UI color to appropriate color
    def toggleCells(self):
        indexes = self.table.selectionModel().selectedIndexes()
        for i in indexes:
            value = 'در دسترس' if self.data[i.row()][i.column()] == 'غیرقابل دسترس' else 'غیرقابل دسترس'
            if value == 'در دسترس':
                self.table.setStyleSheet('selection-background-color: rgb(46, 204, 113); selection-color: black;')
            else:
                self.table.setStyleSheet('selection-background-color: rgb(231, 76, 60); selection-color: black;')
            self.model.setData(i, value)

    def getData(self):
        return self.data

# Timetable model that provides color support for availability status
# TODO: Assess for possible different version of timetable widget
class TimetableModel(TableModel.TableModel):
    def __init__(self, header, data):
        super().__init__(header, data)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role == QtCore.Qt.BackgroundRole:
            if self.data[index.row()][index.column()] == 'در دسترس':
                return QtGui.QBrush(QtGui.QColor(46,204,113))
            else:
                return QtGui.QBrush(QtGui.QColor(231, 76, 60))
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return self.data[index.row()][index.column()]