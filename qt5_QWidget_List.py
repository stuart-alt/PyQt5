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

        self.list = QListWidget()
        self.list.insertItem(0, "Python")
        self.list.insertItem(1, "Java")
        self.list.insertItem(2, "C++")
        self.list.insertItem(3, "C#")
        self.list.insertItem(4, "Ruby")
        self.list.insertItem(5, "Kotlin")
        self.list.clicked.connect(self.listview_clicked)

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)

        vbox.addWidget(self.list)

        self.setLayout(vbox)

        self.show()

    def listview_clicked(self):
        item = self.list.currentItem()
        self.label.setText(str(item.text()))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
