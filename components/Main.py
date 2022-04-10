from qt_ui.v1 import Main
from components import Instructor, Room, Subject, Section, ScenarioManager, ResultViewer



class MainWindow(Main.Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(parent)
        self.connectButtons()
        self.drawTrees()
       # Tab change listener
        self.tabWidget.currentChanged.connect(lambda idx: self.tabListener(idx))
        # Select default tab index
        self.tabWidget.setCurrentIndex(4)
        self.btnScenResult.click()


    # Connect Main component buttons to respective actions
    def connectButtons(self):
        self.btnInstrAdd.clicked.connect(lambda: self.openInstructor())
        self.btnRoomAdd.clicked.connect(lambda: self.openRoom())
        self.btnSubjAdd.clicked.connect(lambda: self.openSubject())
        self.btnSecAdd.clicked.connect(lambda: self.openSection())
        self.btnScenResult.clicked.connect(lambda: self.openResult())

    # Initialize trees and tables
    def drawTrees(self):
        self.instrTree = Instructor.Tree(self.treeInstr)
        self.roomTree = Room.Tree(self.treeRoom)
        self.subjTree = Subject.Tree(self.treeSubj)
        self.secTree = Section.Tree(self.treeSec)
        self.scenTree = ScenarioManager.Tree(self.treeScen)

    # Open Instructor Edit Modal
    def openInstructor(self, id = False):
        Instructor.Instructor(id)
        self.instrTree.display()

    # Open Room Edit Modal
    def openRoom(self, id = False):
        Room.Room(id)
        self.roomTree.display()

    # Open Subject Edit Modal
    def openSubject(self, id = False):
        Subject.Subject(id)
        self.subjTree.display()

    # Open Section Edit Modal
    def openSection(self, id = False):
        Section.Section(id)
        self.secTree.display()

    
    def tabListener(self, index):
        if index == 4:
            self.scenTree.display()

    def openResult(self):
        ResultViewer.ResultViewer()