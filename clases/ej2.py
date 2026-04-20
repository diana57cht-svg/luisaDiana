import math
class FuncionT:
    def __init__(self, dof):
        self.dof = dof

    def evaluar(self, x):
        num = math.gamma((self.dof + 1) / 2)
        den = math.sqrt(self.dof * math.pi) * math.gamma(self.dof / 2)
        return (num / den) * (1 + (x**2) / self.dof) ** (-(self.dof + 1) / 2)

class Simpson:
    def __init__(self, funcion, a, b, n=100):
        self.funcion = funcion
        self.a = a
        self.b = b
        self.n = n if n % 2 == 0 else n + 1
        self.resultado = 0  

    def calcular(self):
        w = (self.b - self.a) / self.n
        suma = self.funcion.evaluar(self.a) + self.funcion.evaluar(self.b)

        for i in range(1, self.n):
            x = self.a + i * w

            if i % 2 == 0:
                suma += 2 * self.funcion.evaluar(x)
            else:
                suma += 4 * self.funcion.evaluar(x)

        self.resultado = (w / 3) * suma  


