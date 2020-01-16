from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Signal and Slots @ stu_dados"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("sair.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createButton()
        self.show()


    def createButton(self):
        button = QPushButton("DON'T click me", self)
        # button.move(50, 50)
        button.setGeometry(QRect(100, 100, 151, 50))  # x and y position - then width and height
        button.setIcon(QtGui.QIcon("sair.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("IT DOESN'T DO ANYTHING!")
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        # print("Hello World")
        sys.exit()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
