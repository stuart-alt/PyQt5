from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLCDNumber
import sys
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - QLCD_Number"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUI()
        self.show()

    def InitUI(self):
        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet('background-color: lightblue')
        # self.lcd.display(23)
        vbox.addWidget(self.lcd)

        self.button = QPushButton("Gerador de número aleatório")
        self.button.clicked.connect(self.LCDHandler)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def LCDHandler(self):
        random = randint(1, 200)
        self.lcd.display(random)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
