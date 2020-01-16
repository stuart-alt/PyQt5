from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QButtonGroup, QHBoxLayout, \
    QLabel, QVBoxLayout, QGroupBox, QRadioButton
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QButton Group @ stu_dados"
        self.top = 500
        self.left = 500
        self.width = 500
        self.height = 200
        self.iconName = "_imagens/stuart.ico"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()
        groupbox = QGroupBox("Select your favorite fruit: ")
        groupbox.setFont(QtGui.QFont("Sanserif", 15))

        hbox.addWidget(groupbox)

        vbox = QVBoxLayout()

        rad1 = QRadioButton("Maça")
        vbox.addWidget(rad1)

        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)

        rad3 = QRadioButton("Melão")
        vbox.addWidget(rad3)

        groupbox.setLayout(vbox)
        self.setLayout(hbox)




        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
