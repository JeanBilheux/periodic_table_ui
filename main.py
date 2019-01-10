import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_periodic_table import Ui_MainWindow as UiMainWindow


class PeriodicTable(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent=parent)
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Define Chemical Formula")

    def accept(self):
        pass

    def reject(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    o_dialog = PeriodicTable()
    o_dialog.show()
    app.exec_()