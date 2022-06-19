from PyQt5 import QtCore, QtWidgets, QtGui
from components import Settings, PreviewTableModel, Utilities
import json
import re



class PreviewScheduleParser:
    # Section / Room View
    # Subject Name + Instructor
    # Instructor View
    # Subject Name + Instructor + Section

    # table = QTableView, data = []
    def __init__(self, table, data, rawData):
        self.table = table
        with open('timeslots.json') as json_file:
            self.timeslots = timeslots = json.load(json_file)['timeslots']
        self.settings = settings = Settings.getSettings()
        header = []
        vertical_header = []
        horizontal_header = []
        timeslot_size = int(self.settings['ending_time'] - self.settings['starting_time'] + 1)
        rooms_size = len(rawData['rooms'])
        dayNames = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]
        
        for day in dayNames:
            for i in range(timeslot_size):
                timeslot_name = self.getRegex(timeslots[i], "\d{1,2}:\d{2}")
                str_header = day + "-" + timeslot_name
                vertical_header.append(str_header)
    
        header.append(vertical_header)

        for i,room in enumerate(rawData['rooms']):
            horizontal_header.append(rawData['rooms'][i+1][0]) 

        header.append(horizontal_header)  

        temporaryData = []
        for i in range(rooms_size):
            temporary_row = ['' for i in vertical_header]
            temporaryData.append(temporary_row)
        self.model = PreviewScheduleParserModel(header, temporaryData)
        table.setModel(self.model)
        table.setFocusPolicy(QtCore.Qt.NoFocus)
        table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        # table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.parseData(data)

    # data = [{'color': None, 'text': '', 'instances': [[day, startingTS, endingTS]]}]
    def parseData(self, data):
        view = self.table
        model = self.model
        for entry in data:
            entry['color'] = Utilities.colorGenerator()
            for instance in entry['instances']:
                index = model.index(instance[1], instance[0])
                view.setSpan(instance[1], instance[0], 1, instance[2])
                item = QtGui.QStandardItem(entry['text'])
                item.setBackground(QtGui.QBrush(QtGui.QColor(*entry['color'])))
                item.setForeground(QtGui.QBrush(QtGui.QColor(*Utilities.textColor(entry['color']))))
                model.setData(index, item)

    def subjectGenerator(self):
        print(self.settings['starting_time'])

    # return single part of string with regex
    def getRegex(self, string, regex):
        return re.search(regex, string).group(0)


class PreviewScheduleParserModel(PreviewTableModel.PreviewTableModel):
    def __init__(self, header, data):
        super().__init__(header, data)

    def setData(self, index, value, role=None):
        if not index.isValid():
            return False
        elif role is None:
            self.data[index.row()][index.column()] = value
        self.dataChanged.emit(index, index, [])
        return True

    def data(self, index, role):
        if not index.isValid() or not self.data[index.row()][index.column()]:
            return QtCore.QVariant()
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter
        elif role == QtCore.Qt.BackgroundRole:
            return self.data[index.row()][index.column()].background()
        elif role == QtCore.Qt.ForegroundRole:
            return self.data[index.row()][index.column()].foreground()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return self.data[index.row()][index.column()].text()