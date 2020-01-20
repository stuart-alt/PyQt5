from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, \
    QGridLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Grid Layout"
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

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("WHAT IS YOU FAVORITE PROGRAMMING LANGUAGE")
        gridLayout = QGridLayout()

        buttonPython = QPushButton("Python!", self)
        buttonPython.setIcon(QtGui.QIcon("_imagens/python.png"))
        buttonPython.setIconSize(QtCore.QSize(20, 20))
        buttonPython.setMinimumHeight(40)
        gridLayout.addWidget(buttonPython, 0, 0)

        buttonPhp = QPushButton("PHP!", self)
        buttonPhp.setIcon(QtGui.QIcon("_imagens/php.png"))
        buttonPhp.setIconSize(QtCore.QSize(20, 20))
        buttonPhp.setMinimumHeight(40)
        gridLayout.addWidget(buttonPhp, 0, 1)

        buttonCpp = QPushButton("C++!", self)
        buttonCpp.setIcon(QtGui.QIcon("_imagens/cplus.png"))
        buttonCpp.setIconSize(QtCore.QSize(20, 20))
        buttonCpp.setMinimumHeight(40)
        gridLayout.addWidget(buttonCpp, 1, 0)

        buttonJavascript = QPushButton("Javascrip!", self)
        buttonJavascript.setIcon(QtGui.QIcon("_imagens/javascript.ico"))
        buttonJavascript.setIconSize(QtCore.QSize(20, 20))
        buttonJavascript.setMinimumHeight(40)
        gridLayout.addWidget(buttonJavascript, 1, 1)

        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
