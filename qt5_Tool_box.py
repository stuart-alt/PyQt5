from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox, QDial, QSpinBox, QDialog, QProgressBar, QToolBox
import sys
from PyQt5.QtCore import Qt


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Tool Box"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setStyleSheet('background-color:lightblue')
        self.InitUI()

        self.show()

    def InitUI(self):
        vbox = QVBoxLayout()

        toolbox = QToolBox()
        # toolbox.setStyleSheet('background-color:white')
        vbox.addWidget(toolbox)

        label = QLabel()
        toolbox.addItem(label, "Python")

        label = QLabel()
        toolbox.addItem(label, "Java")

        label = QLabel()
        toolbox.addItem(label, "C++")

        self.setLayout(vbox)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
