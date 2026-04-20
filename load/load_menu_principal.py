from PyQt5 import QtWidgets, uic
from load.load_psp import psp_1
from load.load_ejer2 import Ventana

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()
        self.actionejer1.triggered.connect(self.ingresarEjercicio)
        self.actionejer2.triggered.connect(self.ingresarEjercicio2)
        self.actionSalir.triggered.connect(self.salir)
    
    def ingresarEjercicio(self):
        vc= psp_1()
        vc.exec()
    
    def ingresarEjercicio2(self):
        vc= Ventana()
        vc.exec()
    
    def salir(self):
        self.close()