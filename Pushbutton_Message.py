from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction
from PyQt5.QtCore import QCoreApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Personalizando o PushButton"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("user.ico"))
        button = QPushButton("Sair", self)
        button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: white; font: bold; border: none}')
        button.setToolTip("Clique para sair")
        button.setToolTipDuration(2000)
        button.move(200, 200)
        button.clicked.connect(self.CloseApp)

        self.InitWindow()

    def InitWindow(self):
        mainMenu = self.menuBar()
        ArquivoMenu = mainMenu.addMenu("Arquivo")
        VisualizarMenu = mainMenu.addMenu("Visualizar")
        EditarMenu = mainMenu.addMenu("Editar")
        PesquisarMenu = mainMenu.addMenu("Pesquisar")
        AjudaMenu = mainMenu.addMenu("Ajuda")

        exitButton = QAction(QIcon("sair.png"), 'Sair', self)
        exitButton.setShortcut("Ctrl+E")
        exitButton.setToolTip("Sair do programa")
        exitButton.triggered.connect(self.close)

        ArquivoMenu.addAction(exitButton)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.statusBar().showMessage("Stu_dados | Todos os direitos reservados.  ;) ")


    def CloseApp(self):
        reply = QMessageBox.question(self, "Stu_dados", "Deseja realmente sair?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.Close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
