from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Layout"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("WHAT IS YOUR FAVORITE SPORT")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Soccer!", self)
        button.setIcon(QtGui.QIcon("_imagens/soccer.png"))
        button.setIconSize(QtCore.QSize(20, 20))
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Baseball!", self)
        button1.setIcon(QtGui.QIcon("_imagens/baseball.png"))
        button1.setIconSize(QtCore.QSize(20, 20))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Tennis!", self)
        button2.setIcon(QtGui.QIcon("_imagens/tennis.jpg"))
        button2.setIconSize(QtCore.QSize(20, 20))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
