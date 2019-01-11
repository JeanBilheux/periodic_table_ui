try:
    from PyQt4.QtGui import QDialog
    from PyQt4 import QtCore, QtGui
except ImportError:
    try:
        from PyQt5.QtWidgets import QDialog
        from PyQt5 import QtCore, QtGui
    except ImportError:
        raise ImportError("Requires PyQt4 or PyQt5")

from ui_isotopes import Ui_Dialog as UiDialog


class IsotopesHandler:

    def __init__(self, parent=None, element=''):

        if parent.isotope_ui is None:
            o_isotope = IsotopeDialog(parent=parent,
                                      element=element)
            o_isotope.show()
            parent.isotope_ui = o_isotope
        else:
            parent.isotope_ui.setFocus()
            parent.isotope_ui.activateWindow()

class IsotopeDialog(QDialog):

    def __init__(self, parent=None, element=''):
        self.parent = parent
        QDialog.__init__(self, parent=parent)
        self.ui = UiDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Select the Isotope of {}".format(element))

        self.init_widgets(element)

    def init_widgets(self, element):
        pass

    def accept(self):
        self.parent.isotope_ui = None
        self.close()

    def reject(self):
        self.parent.isotope_ui = None
        self.close()

    def closeEvent(self, c):
        pass