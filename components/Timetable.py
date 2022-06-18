from PyQt5 import QtCore, QtWidgets, QtGui
from components import Settings, TableModel
import json
import logging


#Creating and Configuring Logger
Log_Format = "%(levelname)s %(asctime)s - %(message)s"


logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.DEBUG,
                    encoding='utf-8')

# Logging Level = debug, info, warning, error

logger = logging.getLogger()


# Used for displaying toggable timetable
class Timetable:
    def __init__(self, table, data=False):
        self.table = table
        header = [['شنبه', 'یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنجشنبه']]
        with open('timeslots.json') as json_file:
            timeslots = json.load(json_file)['timeslots']
        header.append(timeslots)
        self.data = data
        if not data:
            self.data = []
            for i in timeslots:
                self.data.append(['Available', 'Available', 'Available', 'Available', 'Available', 'Available'])
        self.model = TimetableModel(header, self.data)
        table.setModel(self.model)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        table.clicked.connect(self.toggleCells)
        table.horizontalHeader().sectionClicked.connect(self.multiToggleCells)
        table.verticalHeader().sectionClicked.connect(self.multiToggleCells)
        table.findChild(QtWidgets.QAbstractButton).clicked.connect(self.multiToggleCells)
        
    # Toggles the availability and changes UI color to appropriate color
    def multiToggleCells(self):
        indexes = self.table.selectionModel().selectedIndexes()
        counter = 0
        for i in indexes:
            if self.data[i.row()][i.column()] == 'Available':
                counter += 1
            else:
                counter -= 1 
        if counter > 0:
            for i in indexes:
                value = 'Unavailable'
                self.table.setStyleSheet('selection-background-color: rgb(231, 76, 60); selection-color: black;')
                self.model.setData(i, value)
        else:
            for i in indexes:
                value = 'Available'
                self.table.setStyleSheet('selection-background-color: rgb(46, 204, 113); selection-color: black;')
                self.model.setData(i, value)
                     
    # Toggles the availability and changes UI color to appropriate color
    def toggleCells(self):
        indexe = self.table.selectionModel().selectedIndexes()
        if self.data[indexe[0].row()][indexe[0].column()] == 'Unavailable': 
            value = 'Available'
            self.table.setStyleSheet('selection-background-color: rgb(46, 204, 113); selection-color: black;')
        else :
            value = 'Unavailable'
            self.table.setStyleSheet('selection-background-color: rgb(231, 76, 60); selection-color: black;')   
        self.model.setData(indexe[0], value)


    def getData(self):
        return self.data


# Timetable model that provides color support for availability status
class TimetableModel(TableModel.TableModel):
    def __init__(self, header, data):
        super().__init__(header, data)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role == QtCore.Qt.BackgroundRole:
            if self.data[index.row()][index.column()] == 'Available':
                return QtGui.QBrush(QtGui.QColor(46, 204, 113))
            else:
                return QtGui.QBrush(QtGui.QColor(231, 76, 60))
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return self.data[index.row()][index.column()]


def generateRawTable():
    settings = Settings.getSettings()
    data = []
    for i in range(settings['ending_time'] + 1 - settings['starting_time']):
        data.append(['Available', 'Available', 'Available', 'Available', 'Available', 'Available'])
    return data
