from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView, QStackedWidget, QLabel, QDockWidget, QTextEdit, \
    QListWidget, QComboBox
from PyQt5.QtCore import QCoreApplication, Qt
import mysql.connector
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Combo Box"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUi()
        self.show()

    def InitUi(self):
        vbox = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItem("Python")
        self.combo.addItem("C++")
        self.combo.addItem("C#")
        self.combo.addItem("Java")
        self.combo.addItem("Ruby")

        self.combo.currentTextChanged.connect(self.comboChanged)

        self.label = QLabel("Hello")
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setStyleSheet('color:red')

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def comboChanged(self):
        text = self.combo.currentText()
        self.label.setText("You've selected: " + str(text))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
