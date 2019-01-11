import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_periodic_table import Ui_MainWindow as UiMainWindow
from isotopes_handler import IsotopesHandler


class PeriodicTable(QMainWindow):

    isotope_ui = None

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent=parent)
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Define Chemical Formula")

    def reset_text_field(self):
        pass

    def chemical_formula_changed(self, new_formula):
        pass

    def click_button(self, element):
        IsotopesHandler(parent=self, element=element)

    def h_button(self):
        self.click_button('h')

    def li_button(self):
        self.click_button('li')

    def he_button(self):
        self.click_button('he')

    def be_button(self):
        self.click_button('be')

    def b_button(self):
        self.click_button('b')

    def c_button(self):
        self.click_button('c')

    def n_button(self):
        self.click_button('n')

    def o_button(self):
        self.click_button('o')

    def f_button(self):
        self.click_button('f')

    def ne_button(self):
        self.click_button('ne')

    def na_button(self):
        self.click_button('na')

    def mg_button(self):
        self.click_button('mg')

    def al_button(self):
        self.click_button('al')

    def si_button(self):
        self.click_button('si')

    def p_button(self):
        self.click_button('p')

    def s_button(self):
        self.click_button('s')

    def cl_button(self):
        self.click_button('cl')

    def ar_button(self):
        self.click_button('ar')

    def k_button(self):
        self.click_button('k')

    def ca_button(self):
        self.click_button('ca')

    def sc_button(self):
        self.click_button('sc')

    def ti_button(self):
        self.click_button('ti')

    def v_button(self):
        self.click_button('v')

    def cr_button(self):
        self.click_button('cr')

    def mn_button(self):
        self.click_button('mn')

    def fe_button(self):
        self.click_button('fe')

    def co_button(self):
        self.click_button('co')

    def ni_button(self):
        self.click_button('ni')

    def cu_button(self):
        self.click_button('cu')

    def zn_button(self):
        self.click_button('zn')

    def ga_button(self):
        self.click_button('ga')

    def ge_button(self):
        self.click_button('ge')

    def as_button(self):
        self.click_button('as')

    def se_button(self):
        self.click_button('se')

    def br_button(self):
        self.click_button('br')

    def kr_button(self):
        self.click_button('kr')

    def rb_button(self):
        self.click_button('rb')

    def sr_button(self):
        self.click_button('sr')

    def y_button(self):
        self.click_button('y')

    def zr_button(self):
        self.click_button('zr')

    def nb_button(self):
        self.click_button('nb')

    def mo_button(self):
        self.click_button('mo')

    def tc_button(self):
        self.click_button('tc')

    def ru_button(self):
        self.click_button('ru')

    def rh_button(self):
        self.click_button('rh')

    def pd_button(self):
        self.click_button('pd')

    def ag_button(self):
        self.click_button('ag')

    def cd_button(self):
        self.click_button('cd')

    def in_button(self):
        self.click_button('in')

    def sn_button(self):
        self.click_button('sn')

    def sb_button(self):
        self.click_button('sb')

    def te_button(self):
        self.click_button('te')

    def i_button(self):
        self.click_button('i')

    def xe_button(self):
        self.click_button('xe')

    def cs_button(self):
        self.click_button('cs')

    def ba_button(self):
        self.click_button('ba')

    def lu_button(self):
        self.click_button('lu')

    def hf_button(self):
        self.click_button('hf')

    def ta_button(self):
        self.click_button('ta')

    def w_button(self):
        self.click_button('w')

    def re_button(self):
        self.click_button('re')

    def os_button(self):
        self.click_button('os')

    def ir_button(self):
        self.click_button('ir')

    def pt_button(self):
        self.click_button('pt')

    def au_button(self):
        self.click_button('au')

    def hg_button(self):
        self.click_button('hg')

    def tl_button(self):
        self.click_button('tl')

    def pb_button(self):
        self.click_button('pb')

    def bi_button(self):
        self.click_button('bi')

    def po_button(self):
        self.click_button('po')

    def at_button(self):
        self.click_button('at')

    def rn_button(self):
        self.click_button('rn')

    def fr_button(self):
        self.click_button('fr')

    def ra_button(self):
        self.click_button('ra')

    def lr_button(self):
        self.click_button('lr')

    def rf_button(self):
        self.click_button('rf')

    def db_button(self):
        self.click_button('db')

    def sg_button(self):
        self.click_button('sg')

    def bh_button(self):
        self.click_button('bh')

    def hs_button(self):
        self.click_button('hs')

    def mt_button(self):
        self.click_button('mt')

    def ds_button(self):
        self.click_button('ds')

    def rg_button(self):
        self.click_button('rg')

    def cn_button(self):
        self.click_button('cn')

    def nh_button(self):
        self.click_button('nh')

    def fl_button(self):
        self.click_button('fl')

    def mc_button(self):
        self.click_button('mc')

    def lv_button(self):
        self.click_button('lv')

    def ts_button(self):
        self.click_button('ts')

    def og_button(self):
        self.click_button('og')





    def ok(self):
        self.close()

    def cancel(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    o_dialog = PeriodicTable()
    o_dialog.show()
    app.exec_()