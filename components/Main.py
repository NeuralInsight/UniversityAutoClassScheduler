from qt_ui.v1 import Main
from components import Instructor,Room


class MainWindow(Main.Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(parent)
        self.connectButtons()
        self.drawTrees()
        self.tabWidget.setCurrentIndex(3)

    # Connect Main component buttons to respective actions
    def connectButtons(self):
        self.btnInstrAdd.clicked.connect(lambda: self.openInstructor())
        self.btnRoomAdd.clicked.connect(lambda: self.openRoom())

    # Initialize trees and tables
    def drawTrees(self):
        self.instrTree = Instructor.Tree(self.treeInstr)
        self.roomTree = Room.Tree(self.treeRoom)

    # Open Instructor Edit Modal
    def openInstructor(self, id = False):
        Instructor.Instructor(id)
        self.instrTree.display()

    # Open Room Edit Modal
    def openRoom(self, id = False):
        Room.Room(id)
        self.roomTree.display()