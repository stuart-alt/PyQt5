from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox, QDial, QSpinBox, QDialog, QProgressBar, QToolBox, QMenuBar, QAction, QTextEdit, QFontDialog, QColorDialog, \
    QFileDialog, QMessageBox
import sys
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QIcon, QActionEvent
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - QMenuBar"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createEditor()
        self.CreateMenu()

        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        printAction = QAction(QIcon("_imagens/printer.ico"), "Print", self)
        printAction.setShortcut("Ctrl+P")
        printAction.triggered.connect(self.printDialog)
        fileMenu.addAction(printAction)

        printPreviewAction = QAction(QIcon("_imagens/printpreview.ico"), "Preview", self)
        printPreviewAction.setShortcut("Ctrl+I")
        printAction.triggered.connect(self.printPreviewDialog)
        fileMenu.addAction(printPreviewAction)

        pdfAction = QAction(QIcon("_imagens/pdf.ico"), "Export to PDF", self)
        pdfAction.triggered.connect(self.pdfExport)
        fileMenu.addAction(pdfAction)

        exitAction = QAction(QIcon("_imagens/exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+E")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        copyAction = QAction(QIcon("_imagens/copy.png"), "Copy", self)
        copyAction.setShortcut("Ctrl+C")
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon("_imagens/cut.png"), "Cut", self)
        cutAction.setShortcut("Ctrl+X")
        editMenu.addAction(cutAction)

        pasteAction = QAction(QIcon("_imagens/paste.png"), "Paste", self)
        pasteAction.setShortcut("Ctrl+V")
        editMenu.addAction(pasteAction)

        fontAction = QAction(QIcon("_imagens/font.ico"), "Font", self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon("_imagens/color.ico"), "Color", self)
        colorAction.triggered.connect(self.colorDialog)
        viewMenu.addAction(colorAction)

        aboutAction = QAction(QIcon("_imagens/about.ico"), "About", self)
        aboutAction.triggered.connect(self.AboutMessageBox)
        helpMenu.addAction(aboutAction)

        choiceAction = QAction(QIcon("_imagens/choice.ico"), "Choice Message", self)
        choiceAction.triggered.connect(self.choiceMessageBox)
        helpMenu.addAction(choiceAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(printAction)
        toolbar.addAction(printPreviewAction)
        toolbar.addAction(pdfAction)
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(colorAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(aboutAction)
        toolbar.addAction(choiceAction)

    def exitWindow(self):
        self.close()

    def createEditor(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def pdfExport(self):
        fn, _= QFileDialog.getSaveFileName(self, "EXport PDF", None, "PDF files (.pdf);; All Files()")
        if fn != '':
            if QFileInfo(fn).suffix() == "" :fn += '.pdf'

            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

    def AboutMessageBox(self):
        message = QMessageBox.about(self, "About Application", "This is a simple text editor application \
                                                                Licensed under GPL Free Applications \
                                                                Stu_dados ;) ")

    def choiceMessageBox(self):
        message = QMessageBox.question(self, "Choice Message", "Do you like PyQt5?", \
                                       QMessageBox.Yes | QMessageBox.No)

        if message == QMessageBox.Yes:
            self.textEdit.setText("Yes, I like it.")
        else:
            self.textEdit.setText("No, I don't like it.")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
