from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys


from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(700, 600)
    w.move(200, 200)
    p = w.palette()
    p.setColor(w.backgroundRole(), QtCore.Qt.lightGray)
    w.setPalette(p)
    w.setWindowTitle('Simple')

    tableWidget = QTableWidget()
    tableWidget.setRowCount(5)
    tableWidget.setColumnCount(3)
    tableWidget.setItem(0, 0, QTableWidgetItem("Nome"))
    tableWidget.setItem(0, 1, QTableWidgetItem("Telefone"))
    tableWidget.setItem(0, 2, QTableWidgetItem("Email"))

    w.show()

    sys.exit(app.exec_())
