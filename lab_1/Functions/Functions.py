# Описывает пару значений x-y
class FunctionPoint:
    x = 0
    y = 0


# Описывает функцию как набор пар x-y
class Function:

    points = []

    def __init__(self, x0, xn, n):
        step = (xn - x0) / n
        while x0 <= xn:
            fp = FunctionPoint()
            fp.x = x0
            fp.y = self.value(x0)
            self.points.append(fp)
            x0 += step

    # Возвращает значение функции в точке x
    def value(self, x):
        pass

    # Возвращает значение производной функции в точке x
    def derivative(self, x):
        pass


class FirstTaskFunction(Function):

    # Значение функции в точке х
    def value(self, x):
        return float(x ** 3 - 2.1 * (x ** 2) - 2.6 * x + 1.7)

    # Значение производной в точке
    def derivative(self, x):
        # TODO добить для метода секущих
        return 0


