from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self, val):
        super().__init__()

        self.title = "PyQt5 - Scroll Area"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        labelList = []
        buttonList = []

        for i in range(val):
            labelList.append(QLabel("Label"))
            buttonList.append(QPushButton("Click Me"))
            formLayout.addRow(labelList[i], buttonList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(50)
    sys.exit(App.exec())
