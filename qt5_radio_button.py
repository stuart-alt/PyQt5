from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QPushButton, QGroupBox, QRadioButton, \
    QBoxLayout, QMainWindow, QHBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Radio Button"
        self.left = 300
        self.top = 400
        self.width = 400
        self.height = 300
        self.iconName = "_imagens/mouse.ico"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        self.radioButton()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()


    def radioButton(self):
        self.groupBox = QGroupBox("Escolha o seu sexo")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 13))

        hboxLayout = QHBoxLayout()

        self.radioMale = QRadioButton("Masculino")
        self.radioMale.setChecked(True)
        self.radioMale.setIcon(QtGui.QIcon("_imagens/male.jpg"))
        self.radioMale.setIconSize(QtCore.QSize(30, 30))
        self.radioMale.setFont(QtGui.QFont("Sanserif", 13))
        self.radioMale.toggled.connect(self.OnRadioBtn)

        self.radioFemale = QRadioButton("Feminino")
        self.radioFemale.setIcon(QtGui.QIcon("_imagens/female.ico"))
        self.radioFemale.setIconSize(QtCore.QSize(30, 30))
        self.radioFemale.setFont(QtGui.QFont("Sanserif", 13))
        self.radioFemale.toggled.connect(self.OnRadioBtn)

        self.radioNone = QRadioButton("Prefiro não informar")
        self.radioNone.setIcon(QtGui.QIcon("_imagens/none.png"))
        self.radioNone.setIconSize(QtCore.QSize(30, 30))
        self.radioNone.setFont(QtGui.QFont("Sanserif", 13))
        self.radioNone.toggled.connect(self.OnRadioBtn)

        hboxLayout.addWidget(self.radioMale)
        hboxLayout.addWidget(self.radioFemale)
        hboxLayout.addWidget(self.radioNone)

        self.groupBox.setLayout(hboxLayout)

    def OnRadioBtn(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("Selecionado: " + radioBtn.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
