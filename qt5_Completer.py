from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView, QStackedWidget, QLabel, QDockWidget, QTextEdit, \
    QListWidget, QComboBox, QCompleter, QLineEdit
from PyQt5.QtCore import QCoreApplication, Qt
import mysql.connector
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - QCompleter"
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
        names = ["Argentina", "Brasil", "Uruguay", "Japão", "China", "Estados Unidos da America", "Estados Unidos da Arabia"]
        completer = QCompleter(names)

        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        vbox.addWidget(self.lineedit)

        self.setLayout(vbox)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
