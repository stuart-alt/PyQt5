from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView, QStackedWidget, QLabel, QDockWidget, QTextEdit, \
    QListWidget, QComboBox, QCompleter, QLineEdit, QTimeEdit
from PyQt5.QtCore import QCoreApplication, Qt, QTime
import mysql.connector
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Second QDialog"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 300
        self.iconName = "_imagens/mouse.ico"

        self.MyTime()

        self.InitUi()

    def InitUi(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def MyTime(self):
        vbox = QVBoxLayout()
        time = QTime()
        time.setHMS(13, 15, 40)
        timeedit = QTimeEdit()
        timeedit.setFont(QtGui.QFont("Sanserif", 15))
        timeedit.setTime(time)

        vbox.addWidget(timeedit)
        self.setLayout(vbox)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
