from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
# Adicionando um comentário


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Criando tabela em PyQt5"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 250
        self.setWindowIcon(QtGui.QIcon("user.ico"))

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.creatingTables()
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
        self.show()


    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Nome"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Telefone"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Email"))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
