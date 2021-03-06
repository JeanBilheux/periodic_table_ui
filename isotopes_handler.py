import periodictable

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

        self.init_widgets(element)

    def init_widgets(self, element):
        list_isotopes = []
        for iso in getattr(periodictable, element):
            #reformat
            list_str_iso = str(iso).split('-')
            str_iso = "".join(list_str_iso)
            list_isotopes.append(str_iso)

        self.ui.comboBox.addItems(list_isotopes)

    def accept(self):
        isotope_selected = self.ui.comboBox.currentText()
        isotope_number = self.ui.number_of_elements.value()
        self.parent.add_new_entry(isotope=isotope_selected, number=isotope_number)
        self.close()
        self.parent.isotope_ui = None

    def reject(self):
        self.close()
        self.parent.isotope_ui = None

    def closeEvent(self, c):
        pass