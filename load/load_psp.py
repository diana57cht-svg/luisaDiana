from PyQt5 import QtWidgets, uic
from clases.calc import Calcular

class psp_1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp.ui", self)
        self.caso = 1
        self.boton_caso1.clicked.connect(self.caso1)
        self.boton_caso2.clicked.connect(self.caso2)
        self.boton_caso3.clicked.connect(self.caso3)
        self.boton_caso4.clicked.connect(self.caso4)
        self.boton_calcular.clicked.connect(self.botonCalcular)
        self.show()
    
    def caso1(self):
        self.caso = 1

    def caso2(self):
        self.caso = 2

    def caso3(self):
        self.caso = 3

    def caso4(self):
        self.caso = 4

    def botonCalcular(self):
        if self.caso == 1:
            x = [130,650,99,150,128,302,95,945,368,961]
            y = [186,699,132,272,291,331,199,1890,788,1601]
        elif self.caso == 2:
            x = [130,650,99,150,128,302,95,945,368,961]
            y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
        elif self.caso == 3:
            x = [163,765,141,166,137,355,136,1206,433,1130]
            y = [186,699,132,272,291,331,199,1890,788,1601]
        else:
            x = [163,765,141,166,137,355,136,1206,433,1130]
            y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]

        xk = float(self.edit_xk.text())

        cal = Calcular(xk, x, y)
        b0 = cal.calcular_b0()
        b1 = cal.calcular_b1()
        r = cal.calcular_r()
        r2 = cal.calcular_r2()
        yk = cal.predecir_yk()


        self.label_b0.setText(str(b0))
        self.label_b1.setText(str(b1))
        self.label_r.setText(str(r))
        self.label_r2.setText(str(r2))
        self.label_yk.setText(str(yk))

        
