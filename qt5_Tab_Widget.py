from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox, QDial, QSpinBox, QDialog, QProgressBar, QToolBox, QMenuBar, QAction, QTextEdit, QFontDialog, QColorDialog, \
    QFileDialog, QMessageBox, QMenu, QTabWidget, QDialogButtonBox, QCheckBox, QComboBox
import sys
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QIcon, QActionEvent
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class Tab(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Tab Widget"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        tabWidget.addTab(TabContact(), "Contact Details")
        tabWidget.addTab(TabPersonDetails(), "Person Details")
        tabWidget.setFont(QtGui.QFont("Sanserif", 10))

        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonBox)
        self.setLayout(vbox)


class TabContact(QWidget):
    def __init__(self):
        super().__init__()

        name = QLabel("Name: ")
        nameEdit = QLineEdit()
        phone = QLabel("Phone: ")
        phoneEdit = QLineEdit()
        email = QLabel("Email: ")
        emailEdit = QLineEdit()
        address = QLabel("Address: ")
        addressEdit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameEdit)
        vbox.addWidget(phone)
        vbox.addWidget(phoneEdit)
        vbox.addWidget(email)
        vbox.addWidget(emailEdit)
        vbox.addWidget(address)
        vbox.addWidget(addressEdit)
        self.setLayout(vbox)


class TabPersonDetails(QWidget):
    def __init__(self):
        super().__init__()

        groupBox = QGroupBox("Select your gender")

        list = ["Not specified", "Male", "Female"]

        combo = QComboBox()
        combo.addItems(list)

        vbox = QVBoxLayout()
        vbox.addWidget(combo)

        groupBox.setLayout(vbox)

        groupBox2 = QGroupBox("Select you favorite programming language")

        python = QCheckBox("Python")
        cpp = QCheckBox("C++")
        java = QCheckBox("Java")

        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)

        groupBox2.setLayout(vboxp)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox2)

        self.setLayout(mainLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    # window = Window()
    tabDialog = Tab()
    tabDialog.show()
    sys.exit(App.exec())
