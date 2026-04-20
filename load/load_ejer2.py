from PyQt5 import QtWidgets, uic
from clases.ej2 import FuncionT, Simpson

class Ventana(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana2.ui", self)

        self.boton_integrar.clicked.connect(self.integrar)
        self.show()

    def integrar(self):
        x = float(self.lineEdit_x_inicial.text())
        dof = int(self.lineEdit_dof.text())

        f = FuncionT(dof)
        simpson = Simpson(f, 0, x)

        simpson.calcular()

        self.label_resultado.setText(str(simpson.resultado))

        
    