from clases.ej2 import FuncionT
from clases.ej2 import Simpson

# Crear función
funcion = FuncionT(dof)

# ---- PRIMER LLAMADO A LA CLASE ----
simpson = Simpson(funcion, 0, x)
simpson.calcular()
pCalculada = simpson.resultado

# Ajuste inicial
if pCalculada < p:
    x = x + d
else:
    x = x - d

errorSignoAnterior = p - pCalculada

# Ciclo
while True:

    # ---- VOLVER A LLAMAR A LA CLASE ----
    simpson = Simpson(funcion, 0, x)
    simpson.calcular()
    pCalculada = simpson.resultado

    errorSigno = p - pCalculada
    errorSinSigno = abs(errorSigno)

    if errorSinSigno < tolerancia:
        break

    if errorSigno * errorSignoAnterior < 0:
        d = d / 2

    if pCalculada < p:
        x = x + d
    else:
        x = x - d

    errorSignoAnterior = errorSigno


print("x final:", x)
print("p calculada:", pCalculada)
print("error:", errorSinSigno)