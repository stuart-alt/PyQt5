from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow, QPushButton, QDialog, \
    QGroupBox, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Check Box @ stu_dados"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400
        self.iconName = "_imagens/stuart.ico"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateCheckBox()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        self.textBox = QLabel(self)
        self.textBox.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.textBox)

        self.setLayout(vbox)

        self.show()

    def CreateCheckBox(self):
        self.groupbox = QGroupBox("Escolha o seu programa favorito: ")
        self.groupbox.setFont(QtGui.QFont("Sanserif", 13))
        hboxLayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon("_imagens/python.png"))
        self.check1.setIconSize(QtCore.QSize(30, 30))
        self.check1.setFont(QtGui.QFont("Sanserif", 11))
        self.check1.toggled.connect(self.OnCheckBox_Toggled)
        hboxLayout.addWidget(self.check1)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QtGui.QIcon("_imagens/java.ico"))
        self.check2.setIconSize(QtCore.QSize(30, 30))
        self.check2.setFont(QtGui.QFont("Sanserif", 11))
        self.check2.toggled.connect(self.OnCheckBox_Toggled)
        hboxLayout.addWidget(self.check2)

        self.check3 = QCheckBox("C++")
        self.check3.setIcon(QtGui.QIcon("_imagens/cpp.png"))
        self.check3.setIconSize(QtCore.QSize(30, 30))
        self.check3.setFont(QtGui.QFont("Sanserif", 11))
        self.check3.toggled.connect(self.OnCheckBox_Toggled)
        hboxLayout.addWidget(self.check3)

        self.groupbox.setLayout(hboxLayout)

    def OnCheckBox_Toggled(self):
        if self.check1.isChecked():
            self.textBox.setText("Selecionou: " + self.check1.text())

        if self.check2.isChecked():
            self.textBox.setText("Selecionou: " + self.check2.text())

        if self.check3.isChecked():
            self.textBox.setText("Selecionou: " + self.check3.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
