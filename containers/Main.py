from PyQt5 import QtCore,QtWidgets
from containers import Generate, Instructor, ResultViewer, Room, Subject, Section
from components import Settings, Database as db, Timetable, ImportExportHandler as ioHandler
from py_ui import Main
import re
import xlsxwriter
import json
import gc
import pickle
import copy
import csv
import logging
import os
import random



class MainWindow(Main.Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setupUi(parent)
        self.connectButtons()
        self.settings = Settings.getSettings()
        self.loadSettings()
        self.handleSettings()
        self.drawTrees()
        self.tabWidget.currentChanged.connect(self.tabListener)
        self.tabWidget.setCurrentIndex(0)
        self.result = { 'data': [] }
        self.getLastResult()
        self.txtEditInsSearch.textChanged.connect(lambda value: self.instrTree.onSearchTextChanged(value))
        self.txtSearchSubject.textChanged.connect(lambda value: self.subjTree.onSearchTextChanged(value))
        self.txtSearchRoom.textChanged.connect(lambda value: self.roomTree.onSearchTextChanged(value))



    def getLastResult(self):
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT content FROM results WHERE id = (SELECT MAX(id) FROM results)')
        result = cursor.fetchone()
        conn.close()
        if result:
            self.result = pickle.loads(result[0])
            result = self.result
            self.rawData = copy.deepcopy(result['rawData'])

    # Connect Main component buttons to respective actions
    def connectButtons(self):
        self.btnInstrAdd.clicked.connect(lambda: self.openInstructor())
        self.btnRoomAdd.clicked.connect(lambda: self.openRoom())
        self.btnSubjAdd.clicked.connect(lambda: self.openSubject())
        self.btnSecAdd.clicked.connect(lambda: self.openSection())
        self.btnScenResult.clicked.connect(lambda: self.ExportExcelFile())
        self.btnScenGenerate.clicked.connect(lambda: self.openGenerate())
        self.btnInstrImport.clicked.connect(self.importInstructors)
        self.btnRoomImport.clicked.connect(self.importRooms)
        self.btnSubjImport.clicked.connect(self.importSubjects)
        self.actionSave_As.triggered.connect(self.saveAs)
        self.actionOpen.triggered.connect(self.load)
        self.actionSettings.triggered.connect(lambda: self.tabWidget.setCurrentIndex(4))
        # self.actionExit.triggered.connect(exit)
        self.actionNew.triggered.connect(lambda: self.new())

    # Initialize trees and tables
    def drawTrees(self):
        self.instrTree = Instructor.Tree(self.treeInstr)
        self.roomTree = Room.Tree(self.treeRoom)
        self.subjTree = Subject.Tree(self.treeSubj)
        self.secTree = Section.Tree(self.treeSec)

    # Handle component openings

    def openInstructor(self, id=False):
        Instructor.Instructor(id)
        self.instrTree.display()

    def openRoom(self, id=False):
        Room.Room(id)
        self.roomTree.display()

    def openSubject(self, id=False):
        Subject.Subject(id)
        self.subjTree.display()

    def openSection(self, id=False):
        Section.Section(id)
        self.secTree.display()

    def tabListener(self, index):
        self.instrTree.display()
        self.roomTree.display()
        self.subjTree.display()
        self.secTree.display()
        if index == 4:
            self.checkContents()

    def checkContents(self):
        conn = db.getConnection()
        cursor = conn.cursor()
        disabled = False
        cursor.execute('SELECT id FROM rooms LIMIT 1')
        if cursor.fetchone():
            disabled = True
        cursor.execute('SELECT id FROM instructors LIMIT 1')
        if cursor.fetchone():
            disabled = True
        cursor.execute('SELECT id FROM sections LIMIT 1')
        if cursor.fetchone():
            disabled = True
        cursor.execute('SELECT id FROM subjects LIMIT 1')
        if cursor.fetchone():
            disabled = True
        self.btnScenGenerate.setDisabled(not disabled)
        conn.close()

    def openResult(self):
        # ResultViewer.ResultViewer()
        pass

    # Function to print Excel column name
    # for a given column number
    def findColName(self, n):
        colName = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            colName = chr(65 + remainder) + colName
        return colName
    
    # Create Random Color Hex Code
    def randomColor(self):
        r = lambda: random.randint(0,255)
        return '#%02X%02X%02X' % (r(),r(),r())

    # find dark color by hex code
    def findDarkColor(self, hex):
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:7], 16)
        if (r + g + b) > 350:
            return '#000000'
        else:
            return '#ffffff'

    # return single part of string with regex
    def getRegex(self, string, regex):
        return re.search(regex, string).group(0)

            
    # Export Result to Excel file
    def ExportExcelFile(self):

        # Get Last result data
        self.getLastResult()
        
        #Creating and Configuring Logger
        Log_Format = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename = "mainlog.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.DEBUG,
                    encoding='utf-8')

        # Logging Level = debug, info, warning, error
        mainlogger = logging.getLogger()
        mainlogger.info("init Main")
        
        directory = QtWidgets.QFileDialog().getExistingDirectory(None, 'Select Directory for Export')
        if not directory:
            return False

        # remove old files before create new one
        for file in os.listdir(directory):
            if file == "section_schedule.xlsx":
                os.remove(os.path.join(directory, file))
        # Create new xlsx file
        workbook = xlsxwriter.Workbook('{}/section_schedule.xlsx'.format(directory))
        worksheet = workbook.add_worksheet()
        # Set WorkSheet right-to-left
        worksheet.right_to_left()
        # Add column names
        with open('timeslots.json') as json_file:
            timeslots = json.load(json_file)['timeslots']
        rawData = self.rawData
        mainlogger.info("result: {}".format(self.result['data']))
        chromosome = self.result['data'][-1]
        timeslot_size = int(self.settings['ending_time'] - self.settings['starting_time'] + 1)
        number_of_rooms = len(rawData['rooms']) + 1
        dayNames = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنچشنبه"]
        col_num = 0
        last_index = 2
        first_letter = ""
        last_letter = ""
        for day in dayNames:
            first_index = last_index
            last_index += timeslot_size - 1
            first_letter = self.findColName(first_index)
            last_letter = self.findColName(last_index)
            row_col = "{}1:{}1".format(first_letter, last_letter)
            bg_color = self.randomColor()
            fg_color = self.findDarkColor(bg_color)
            days_cell_format = workbook.add_format({'bg_color' : bg_color,
                                                        'font_color' : fg_color,
                                                        'align' : 'center',
                                                        'valign' : 'vcenter',
                                                        'border' : 1,
                                                        'bold' : True,
                                                        'font_size' : 15})
            worksheet.merge_range(row_col, day, days_cell_format)
            timeslot_cell_format = workbook.add_format({'bg_color' : bg_color,
                                                        'font_color' : fg_color,
                                                        'align' : 'right',
                                                        'valign' : 'vcenter',
                                                        'border' : 1,
                                                        'bold' : True,
                                                        'font_size' : 10})
            for i in range(timeslot_size):
                worksheet.write(1, first_index+i-1, self.getRegex(timeslots[i], "\d{1,2}:\d{2}"), timeslot_cell_format)
            last_index += 1
        rooms_cell_format = workbook.add_format({'bg_color' : "#fcba03",
                                                        'font_color' : '#000000',
                                                        'align' : 'center',
                                                        'valign' : 'vcenter',
                                                        'border' : 1,
                                                        'bold' : True,
                                                        'font_size' : 13})
        for i,room in enumerate(rawData['rooms']):
            worksheet.write(i+2, 0, rawData['rooms'][i+1][0], rooms_cell_format)

        number_of_subjects = 0
        for section, subjects in chromosome['sections'].items():
            schedule = {day: [[] for i in range(number_of_rooms)] for day in range(len(dayNames))}
            for subject, details in subjects['details'].items():

                if not len(details):
                    continue
                number_of_subjects += 1
                instructor = '' if not details[1] else rawData['instructors'][details[1]][0]
                room = details[0]
                course_unit = details[4]
                for day in details[2]:
                    course_name = "id = {}\n{}\n{}\n{}".format(subject,
                                                                        rawData['subjects'][subject][0],
                                                                        rawData['subjects'][subject][2],
                                                                        instructor)
                    schedule[day][room].append({"name" : course_name, "startingTimeslot" : details[3], "unit" :  course_unit})
            
            mainlogger.debug("Number of the course: {}".format(number_of_subjects))

            for day in range(len(dayNames)):
                for room in range(number_of_rooms):
                    day_room_schedule = schedule[day][room]
                    if not len(day_room_schedule):
                        continue 
                    for course in day_room_schedule:
                        c_name = course['name']
                        col_num = course['startingTimeslot'] + 2
                        row_num = room + 2
                        c_unit = course['unit']
                        first_index = day*timeslot_size+col_num
                        first_letter = self.findColName(first_index)
                        last_letter = self.findColName(first_index + c_unit - 1)
                        row_col = "{}{}:{}{}".format(first_letter, row_num, last_letter, row_num)
                        bg_color = self.randomColor()
                        fg_color = self.findDarkColor(bg_color)
                        course_cell_format = workbook.add_format({'bg_color' : bg_color, 
                                                                        "font_color" : fg_color,
                                                                        'align' : 'center',
                                                                        'valign' : 'vcenter',
                                                                        'border' : 1,
                                                                        'font_size' : 12,
                                                                        'text_wrap' : True})
                                                                        
                        worksheet.merge_range(row_col, c_name, course_cell_format)
                    

        worksheet.set_column(1, last_index, 10)
        for i in range(number_of_rooms + 2):
            worksheet.set_row(i+2, 70)
        workbook.close()
        
            # for row_num, row_data in enumerate(schedule):
            #     for col_num, col_data in enumerate(row_data):
            #         worksheet.write(row_num, col_num, col_data)

            
            #for timeslot in range(self.settings['starting_time'], self.settings['ending_time'] + 1):
                #writer.writerow([timeslots[timeslot], *schedule[timeslot - self.settings['starting_time']]])
            #writer.writerow([''])
        
        # Create schedule for instructors
        # with open('{}/instructors_schedule.csv'.format(directory), 'w', newline='', encoding="utf-8") as file:
        #     writer = csv.writer(file, dialect='excel')
        #     for instructor in rawData['instructors'].keys():
        #         writer.writerow([rawData['instructors'][instructor][0]])
        #         writer.writerow(dayNames)
        #         schedule = [['' for j in range(6)] for i in
        #                     range(self.settings['ending_time'] - self.settings['starting_time'] + 1)]
        #         for section, subjects in chromosome['sections'].items():
        #             for subject, details in subjects['details'].items():
        #                 if not len(details) or details[1] != instructor:
        #                     continue
        #                 for timeslot in range(details[3], details[3] + details[4]):
        #                     for day in details[2]:
        #                         schedule[timeslot][day] = '{} - {} - {}'.format(rawData['subjects'][subject][2],
        #                                                                         rawData['rooms'][details[0]][0],
        #                                                                         rawData['sections'][section][0])
        #             for timeslot in range(self.settings['starting_time'], self.settings['ending_time'] + 1):
        #                 writer.writerow([timeslots[timeslot], *schedule[timeslot - self.settings['starting_time']]])
        #         writer.writerow([''])
        # # Create schedule for rooms
        # with open('{}/rooms_schedule.csv'.format(directory), 'w', newline='', encoding="utf-8") as file:
        #     writer = csv.writer(file, dialect='excel')
        #     for room in rawData['rooms'].keys():
        #         writer.writerow([rawData['rooms'][room][0]])
        #         writer.writerow(dayNames)
        #         schedule = [['' for j in range(6)] for i in
        #                     range(self.settings['ending_time'] - self.settings['starting_time'] + 1)]
        #         for section, subjects in chromosome['sections'].items():
        #             for subject, details in subjects['details'].items():
        #                 if not len(details) or details[0] != room:
        #                     continue
        #                 instructor = '' if not details[1] else rawData['instructors'][details[1]][0]
        #                 for timeslot in range(details[3], details[3] + details[4]):
        #                     for day in details[2]:
        #                         schedule[timeslot][day] = '{} - {} - {}'.format(rawData['subjects'][subject][2],
        #                                                                         rawData['sections'][section][0],
        #                                                                         instructor)
        #         for timeslot in range(self.settings['starting_time'], self.settings['ending_time'] + 1):
        #             writer.writerow([timeslots[timeslot], *schedule[timeslot - self.settings['starting_time']]])
        #         writer.writerow([''])
    
    def openGenerate(self):
        gc.collect()
        result = Generate.Generate()
        if not len(result.topChromosomes):
            return False
        self.openResult()

    def importInstructors(self):
        # instructors = ioHandler.getCSVFile('instructors')
        # if instructors:
        #     instructors.pop(0)
        #     instructors.pop(0)
        #     blankSchedule = json.dumps(Timetable.generateRawTable())
        #     for instructor in instructors:
        #         Instructor.Instructor.insertInstructor([instructor[0], float(instructor[1]), blankSchedule])
        #     self.tabListener(0)
        pass

    def importRooms(self):
        # rooms = ioHandler.getCSVFile('rooms')
        # if rooms:
        #     rooms.pop(0)
        #     rooms.pop(0)
        #     blankSchedule = json.dumps(Timetable.generateRawTable())
        #     for room in rooms:
        #         Room.Room.insertRoom([room[0], blankSchedule, room[1]])
        #     self.tabListener(1)
        pass

    def importSubjects(self):
        # subjects = ioHandler.getCSVFile('subjects')
        # if subjects:
        #     subjects.pop(0)
        #     subjects.pop(0)
        #     for subject in subjects:
        #         Subject.Subject.insertSubject(
        #             [subject[1], float(subject[3]), subject[0], '', json.dumps([]), int(subject[4]), subject[2]])
        # self.tabListener(2)
        pass

    def saveAs(self):
        ioHandler.saveAs()

    def load(self):
        ioHandler.load()
        self.tabWidget.setCurrentIndex(0)
        self.tabListener(0)

    def loadSettings(self):
        if self.settings['lunchbreak']:
            self.radioLunchYes.setChecked(True)
        else:
            self.radioLunchNo.setChecked(True)
        self.editMinPop.setValue(self.settings['minimum_population'])
        self.editMaxPop.setValue(self.settings['maximum_population'])
        self.editMaxGen.setValue(self.settings['maximum_generations'])
        self.editMaxCreation.setValue(self.settings['generation_tolerance'])
        self.editMut.setValue(self.settings['mutation_rate_adjustment_trigger'])
        self.editBaseMut.setValue(self.settings['mutation_rate_base'])
        self.editMutStep.setValue(self.settings['mutation_rate_step'])
        self.editMaxFit.setValue(self.settings['maximum_fitness'])
        self.editElite.setValue(int(self.settings['elite_percent'] * 100))
        self.editDev.setValue(self.settings['deviation_tolerance'])
        self.matrix = matrix = self.settings['evaluation_matrix']
        self.editSbj.setValue(matrix['subject_placement'])
        self.editIdle.setValue(matrix['idle_time'])
        self.matrixSum = sum(matrix.values())
        self.lblTotal.setText('Total: {}%'.format(self.matrixSum))

    # Handle Settings
    def handleSettings(self):
        self.radioLunchYes.toggled.connect(lambda state: self.updateSettings('lunchbreak', state))
        self.editMinPop.valueChanged.connect(self.handleMinPop)
        self.editMaxPop.valueChanged.connect(self.handleMaxPop)
        self.editMaxGen.valueChanged.connect(lambda value: self.updateSettings('maximum_generations', value))
        self.editMaxCreation.valueChanged.connect(lambda value: self.updateSettings('generation_tolerance', value))
        self.editMut.valueChanged.connect(
            lambda value: self.updateSettings('mutation_rate_adjustment_trigger', round(value, 2)))
        self.editBaseMut.valueChanged.connect(
            lambda value: self.updateSettings('mutation_rate_base', round(value, 2)))
        self.editMutStep.valueChanged.connect(
            lambda value: self.updateSettings('mutation_rate_step', round(value, 2)))
        self.editMaxFit.valueChanged.connect(lambda value: self.updateSettings('maximum_fitness', value))
        self.editElite.valueChanged.connect(lambda value: self.updateSettings('elite_percent', round(value / 100, 2)))
        self.editDev.valueChanged.connect(lambda value: self.updateSettings('deviation_tolerance', value))
        self.editSbj.valueChanged.connect(lambda value: self.handleMatrix('subject_placement', value, self.editSbj))
        self.editIdle.valueChanged.connect(lambda value: self.handleMatrix('idle_time', value, self.editIdle))

    def handleStartingTime(self, time):
        if time.hour() * 2 >= self.settings['ending_time']:
            self.timeStarting.setTime(QtCore.QTime(int(self.settings['starting_time'] / 2), 0))
        else:
            self.updateSettings('starting_time', time.hour() * 2)

    def handleEndingTime(self, time):
        if (time.hour() * 2) - 1 <= self.settings['starting_time']:
            self.timeEnding.setTime(QtCore.QTime(int(self.settings['ending_time'] / 2) + 1, 0))
        else:
            self.updateSettings('ending_time', (time.hour() * 2) - 1)

    def handleMinPop(self, value):
        if value > self.settings['maximum_population']:
            self.editMinPop.setValue(self.settings['minimum_population'])
        else:
            self.updateSettings('minimum_population', value)

    def handleMaxPop(self, value):
        if value < self.settings['minimum_population']:
            self.editMaxPop.setValue(self.settings['maximum_population'])
        else:
            self.updateSettings('maximum_population', value)

    def handleMatrix(self, key, value, obj):
        difference = self.matrix[key] - value
        if self.matrixSum - difference > 100:
            obj.setValue(self.matrix[key])
        else:
            self.updateSettings('evaluation_matrix', value, key)
        self.matrixSum = sum(self.settings['evaluation_matrix'].values())
        self.matrix = self.settings['evaluation_matrix']
        self.lblTotal.setText('Total: {}%'.format(self.matrixSum))

    def updateSettings(self, key, value, secondKey=False):
        Settings.setSettings(key, value, secondKey)
        self.settings = Settings.getSettings()

    def onInsSearchChanged(self,value):
        self.instrTree.onSearchTextChanged(value)

    def new(self):
        ioHandler.removeTables()
        db.setup()
        self.tabListener(0)
