from PyQt5 import QtCore
import logging as log_engine

Log_Format = "%(levelname)s %(asctime)s - %(message)s"


log_engine.basicConfig(filename = "tablelog.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = log_engine.DEBUG,
                    encoding='utf-8')

# Logging Level = debug, info, warning, error

table_logger = log_engine.getLogger()

table_logger.info("init PreviewTableModel")

# Standard table model requires 2D header and complete dataset
class PreviewTableModel(QtCore.QAbstractTableModel):
    def __init__(self, header, data):
        super().__init__()
        self.data = data
        self.header = header

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return self.data[index.row()][index.column()]

    def rowCount(self, parent=None, *args, **kwargs):
        table_logger.debug("rowCount: {}".format(len(self.data)))
        return len(self.data)

    def columnCount(self, parent=None, *args, **kwargs):
        table_logger.debug("columnCount: {}".format(len(self.data[0])))
        return len(self.data[0])

    def headerData(self, p_int, Qt_Orientation, role=None):
        if Qt_Orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.header[0][p_int])
        elif Qt_Orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.header[1][p_int])
        return QtCore.QVariant()

    def setData(self, index, value, role=None):
        if not index.isValid():
            return False
        self.data[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True
