class Calcular(object):
    def __init__(self, xk, listax, listay):
        self.xk = xk
        self.x = listax
        self.y = listay

    def contar(self):
        contador = 0
        for _ in self.x:
            contador += 1
        return contador

    def sumatorias(self):
        sum_x = 0
        sum_y = 0
        sum_xy = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0

        for i in range(self.contar()):
            sum_x += self.x[i]
            sum_y += self.y[i]
            sum_xy += self.x[i] * self.y[i]
            sum_x2 += self.x[i] * self.x[i]
            sum_y2 += self.y[i] * self.y[i]
            n += 1

        return sum_x, sum_y, sum_xy, sum_x2, sum_y2, n


    def calcular_b1(self):
        sum_x, sum_y, sum_xy, sum_x2, _, n = self.sumatorias()

        b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
        return b1


    def calcular_b0(self):
        sum_x, sum_y, _, _, _, n = self.sumatorias()

        x_prom = sum_x / n
        y_prom = sum_y / n

        b1 = self.calcular_b1()
        b0 = y_prom - b1 * x_prom

        return b0

    def calcular_r(self):
        sum_x, sum_y, sum_xy, sum_x2, sum_y2, n = self.sumatorias()

        numerador = n * sum_xy - sum_x * sum_y
        denominador = ((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y)) ** 0.5

        r = numerador / denominador
        return r

    def calcular_r2(self):
        r = self.calcular_r()
        return r * r

    def predecir_yk(self):
        b0 = self.calcular_b0()
        b1 = self.calcular_b1()

        yk = b0 + b1 * self.xk
        return yk
  
