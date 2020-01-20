from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox, QDial, QSpinBox
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - QSpinBox"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.spin_changed)
        vbox.addWidget(self.spinBox)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def spin_changed(self):
        spinValue = self.spinBox.value()
        self.label.setText("Valor é: " + str(spinValue))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
