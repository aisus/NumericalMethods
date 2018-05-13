import numpy as np
import math as m
from matplotlib import pyplot as pl


def f(x, y):
    return 1 + (1 - x) * y - (1.5 + x) * y


def runge2():
    h = 0.1
    x = np.empty(4)
    y = np.empty(4)
    x[0] = 0
    y[0] = 2
    i = 0
    while i < 3:
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h, y[i] - k1 + 2 * k2)
        y[i + 1] = y[i] + 1 / 6 * (k1 + 4 * k2 + k3)
        x[i + 1] = x[i] + h
        i += 1
    g = np.linspace(x[2], x[3], 100)
    d = np.linspace(y[2], y[3], 100)
    pl.plot(g, d, 'r', label=u'Р-К третьего порядка')
    pl.legend()


def runge3():
    h = 0.1
    x = np.empty(4)
    y = np.empty(4)
    x[0] = 0
    y[0] = 2
    i = 0
    while i < 3:
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x[i + 1] = x[i] + h
        i += 1
    g = np.linspace(x[2], x[3], 100)
    d = np.linspace(y[2], y[3], 100)
    pl.plot(g, d, 'b', label=u'Р-К четвертого порядка')
    pl.legend()


def forecast():
    h = 0.1
    x = np.empty(4)
    y = np.empty(4)
    x[0] = 0
    y[0] = 2
    i = 0
    while i < 3:
        prog = y[i] + (h ** 2) * f(x[i], y[i])
        y[i + 1] = y[i] + h * f(x[i], y[i]) + (f(x[i] + h ** 2, prog) - f(x[i], y[i])) / 2
        x[i + 1] = x[i] + h
        i += 1
    g = np.linspace(x[2], x[3], 100)
    d = np.linspace(y[2], y[3], 100)
    pl.plot(g, d, 'g--', label=u'Метод прогноза и коррекции')
    pl.legend()


def run():
    y0 = 2
    h = 0.1
    eps = 10 ** -5

    runge2()
    runge3()
    forecast()
    pl.grid()
    pl.show()


if __name__ == '__main__':
    run()
