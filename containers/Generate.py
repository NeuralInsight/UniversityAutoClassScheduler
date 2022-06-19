from PyQt5 import QtCore, QtWidgets
from components import Database as db, ResourceTracker, PreviewScheduleParser, ScenarioComposer, GeneticAlgorithm, Settings
from py_ui import Generate as Parent
from sqlite3 import Binary
from numpy import mean
import pickle
import copy
import logging as preview_log_engine

Log_Format = "%(levelname)s %(asctime)s - %(message)s"


preview_log_engine.basicConfig(filename = "previewlog.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = preview_log_engine.DEBUG,
                    encoding='utf-8')

# Logging Level = debug, info, warning, error

preview_logger = preview_log_engine.getLogger()

preview_logger.info("init PreviewTableModel")


class Generate:
    def __init__(self):
        self.totalResource = {
            'cpu': [],
            'memory': []
        }
        self.tick = 0
        self.data = {
            'results': [],
            'rooms': [],
            'instructors': [],
            'sections': [],
            'sharings': [],
            'subjects': []
        }
        self.topChromosomes = []
        self.meta = []
        self.preview = True
        self.sectionKeys = []
        self.settings = settings = Settings.getSettings()
        composer = ScenarioComposer.ScenarioComposer()
        composer = composer.getScenarioData()
        self.data.update(composer)
        self.dialog = dialog = QtWidgets.QDialog(parent=None)
        # Initialize custom dialog
        self.parent = parent = Parent.Ui_Dialog()
        # Add parent to custom dialog
        parent.setupUi(dialog)
        dialog.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
        self.time = QtCore.QTime(0, 0)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.running = True
        self.table = parent.tableSchedule
        parent.btnPause.clicked.connect(self.togglePause)
        parent.btnStop.clicked.connect(self.stopOperation)
        parent.chkPreview.clicked.connect(self.togglePreview)
        parent.cmbSection.clear()
        for section, details in self.data['sections'].items():
            self.sectionKeys.append(section)
            parent.cmbSection.addItem(details[0])
        parent.cmbSection.currentIndexChanged.connect(self.changePreview)
        self.updateProgressBar(0)
        self.startWorkers()
        dialog.exec_()

    def togglePreview(self, state):
        self.preview = not state

    def togglePause(self):
        self.toggleState()
        self.parent.btnPause.setText('متوقف کردن اجرا' if self.running else 'ادامه فرآیند اجرا')

    def toggleState(self, state=None):
        self.running = (not self.running) if state is None else state
        self.resourceWorker.running = self.running
        self.geneticAlgorithm.running = self.running

    def startWorkers(self):
        self.resourceWorker = ResourceTrackerWorker()
        self.resourceWorker.signal.connect(self.updateResource)
        self.resourceWorker.start()
        self.geneticAlgorithm = GeneticAlgorithm.GeneticAlgorithm(self.data)
        self.geneticAlgorithm.statusSignal.connect(self.updateStatus)
        self.geneticAlgorithm.detailsSignal.connect(self.updateDetails)
        self.geneticAlgorithm.dataSignal.connect(self.updateView)
        self.geneticAlgorithm.operationSignal.connect(self.updateOperation)
        self.geneticAlgorithm.progressBarSignal.connect(self.updateProgressBar)
        self.geneticAlgorithm.progressSignal.connect(self.updateProgressStatus)
        self.geneticAlgorithm.start()

    def updateStatus(self, status):
        self.parent.lblStatus.setText('وضعیت: {}'.format(status))

    def updateDetails(self, details):
        self.parent.boxGen.setTitle('نسل #{}'.format(details[0]))
        self.parent.lblPopulation.setText('جمعیت: {}'.format(details[1]))
        self.parent.lblMutation.setText('نرخ  فعلی جهش: {}%'.format(details[2]))
        self.parent.lblFitness.setText('میانگین فیتنس: {:.2f}%'.format(round(details[3], 2)))
        self.parent.lblPreviousFitness.setText('میانگین فیتنس نسل قبل: {:.2f}%'.format(round(details[4], 2)))
        self.parent.lblHighestFitness.setText('بالاترین فیتنس: {:.2f}%'.format(round(details[5], 2)))
        self.parent.lblLowestFitness.setText('پایین ترین فیتنس: {:.2f}%'.format(round(details[6], 2)))

    def updateView(self, chromosomes):
        chromosomes.reverse()
        self.topChromosomes = copy.deepcopy(chromosomes)
        self.changePreview(self.parent.cmbSection.currentIndex())

    def changePreview(self, index):
        data = []
        if not len(self.topChromosomes) or not self.preview:
            return False
        sections = self.topChromosomes[0][0].data['sections']
        rawData = self.data
        subjects = sections[self.sectionKeys[index]]['details']
        timeslot_size = int(self.settings['ending_time'] - self.settings['starting_time'] + 1)
        for subject, details in subjects.items():
            if not len(details):
                continue
            preview_logger.debug("Preview detail: {}".format(details))
            instructor = '' if not details[1] else rawData['instructors'][details[1]][0]
            instances = []
            for day in details[2]:
                column = day*timeslot_size+details[3]
                row = details[0]
                span_size = details[4]
                instances.append([row, column, span_size])
            data.append({'color': None, 'text': '{} \n {} \n {}'.format(rawData['subjects'][subject][0],
                                                                        rawData['rooms'][details[0]][0],
                                                                        instructor),
                         'instances': instances})
        preview_logger.debug("Preview data: {}".format(data))
        self.loadTable(data, rawData)

    def loadTable(self, data=[], rawData=[]):
        self.table.reset()
        self.table.clearSpans()
        PreviewScheduleParser.PreviewScheduleParser(self.table, data, rawData)

    def updateOperation(self, type):
        if type == 1:
            self.stopOperation()

    def updateTime(self):
        self.time = self.time.addSecs(1)
        self.parent.lblTime.setText('زمان سپری شده: {}'.format(self.time.toString('hh:mm:ss')))

    def stopOperation(self):
        self.geneticAlgorithm.terminate()
        self.geneticAlgorithm.runThread = False
        self.resourceWorker.terminate()
        self.resourceWorker.runThread = False
        self.toggleState(False)
        self.timer.stop()
        if len(self.topChromosomes):
            self.parent.btnStop.setText('بستن')
            self.parent.btnStop.clicked.disconnect(self.stopOperation)
            self.parent.btnStop.clicked.connect(self.dialog.close)
            self.parent.lblCPU.setText('پردازنده: پایان عملیات')
            self.parent.lblMemory.setText('حافظه رم: پایان عملیات')
            self.parent.lblStatus.setText('وضعیت: پایان عملیات')
            self.totalResource['cpu'] = mean(self.totalResource['cpu'])
            self.totalResource['memory'] = mean(self.totalResource['memory'])
            self.meta = [[chromosome[1], chromosome[0].fitnessDetails] for chromosome in
                         self.topChromosomes]
            conn = db.getConnection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO results (content) VALUES (?)', [Binary(
                pickle.dumps({'data': [chromosome[0].data for chromosome in self.topChromosomes],
                              'meta': self.meta,
                              'time': self.time.toString('hh:mm:ss'),
                              'resource': self.totalResource,
                              'rawData': self.data},
                             pickle.HIGHEST_PROTOCOL))])
            conn.commit()
            conn.close()
            self.updateProgressBar(100)
        else:
            self.dialog.close()

    def updateResource(self, resource):
        self.tick += 1
        if self.tick == 3:
            self.tick = 0
        else:
            self.totalResource['cpu'].append(resource[0])
            self.totalResource['memory'].append(resource[1][1])
        self.parent.lblCPU.setText('پردازنده: {}%'.format(resource[0]))
        self.parent.lblMemory.setText('حافظه رم:‌ {}% - {} MB'.format(resource[1][0], resource[1][1]))

    def updateProgressBar(self, progress):
        self.parent.progressBar.setValue(progress)

    def updateProgressStatus(self, status):
        self.parent.lblProgressStatus.setText("مرحله: {}".format(status))



class ResourceTrackerWorker(QtCore.QThread):
    signal = QtCore.pyqtSignal(object)
    running = True
    runThread = True

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.wait()

    def run(self):
        while (self.runThread):
            self.sleep(1)
            if self.running is True:
                cpu = ResourceTracker.getCPUUsage()
                memory = ResourceTracker.getMemoryUsage()
                memory = [ResourceTracker.getMemoryPercentage(memory), ResourceTracker.byteToMegabyte(memory[0])]
                self.signal.emit([cpu, memory])
        return True
