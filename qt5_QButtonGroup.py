from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QButtonGroup, QHBoxLayout, \
    QLabel
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
        self.height = 500
        self.iconName = "_imagens/stuart.ico"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(self.label)


        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton("Python")
        self.buttongroup.addButton(button, 1)
        button.setFont(QtGui.QFont("Sanserif", 13))
        hbox.addWidget(button)

        button = QPushButton("Java")
        self.buttongroup.addButton(button, 2)
        button.setFont(QtGui.QFont("Sanserif", 13))
        hbox.addWidget(button)

        button = QPushButton("C++")
        self.buttongroup.addButton(button, 3)
        button.setFont(QtGui.QFont("Sanserif", 13))
        hbox.addWidget(button)

        self.setLayout(hbox)

        self.show()

    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + " foi clicado.")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
