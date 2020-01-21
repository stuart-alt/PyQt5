from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox, QDial
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - QDial"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dial_changed)

        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def dial_changed(self):
        getValue = self.dial.value()
        self.label.setText("Dial changed to " + str(getValue))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
