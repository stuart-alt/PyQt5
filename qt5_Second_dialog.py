from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView, QStackedWidget, QLabel, QDockWidget, QTextEdit, \
    QListWidget, QComboBox, QCompleter, QLineEdit
from PyQt5.QtCore import QCoreApplication, Qt
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

        self.InitUi()

    def InitUi(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.btn = QPushButton("Open second dialog")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.openSecondDialog)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.show()

    def openSecondDialog(self):
        '''Primeira maneira '''
        mydialog = QDialog()
        mydialog.setModal(True)
        mydialog.exec()

        '''Segunda maneira
        mydialog = QDialog(self)'''

        mydialog.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
