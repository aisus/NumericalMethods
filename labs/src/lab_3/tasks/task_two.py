import numpy as np
import math as m
from matplotlib import pyplot as pl


def f(x, y):
    return 1 + (1 - x) * y - (1.5 + x) * y


def runge_kutta_3(h, n, x0, y0):
    x = np.empty(n)
    y = np.empty(n)
    x[0] = x0
    y[0] = y0
    i = 0
    while i < n-1:
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h, y[i] - k1 + 2 * k2)
        y[i + 1] = y[i] + 1 / 6 * (k1 + 4 * k2 + k3)
        x[i + 1] = x[i] + h
        i += 1
    g = np.linspace(x[0], x[-1], 100)
    d = np.linspace(y[0], y[-1], 100)
    pl.plot(g, d, 'r', label=u'Р-К третьего порядка')
    pl.legend()


def runge_kutta_4(h, n, x0, y0):
    x = np.empty(n)
    y = np.empty(n)
    x[0] = x0
    y[0] = y0
    i = 0
    while i < n-1:
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x[i + 1] = x[i] + h
        i += 1
    g = np.linspace(x[0], x[-1], 100)
    d = np.linspace(y[0], y[-1], 100)
    pl.plot(g, d, 'b', label=u'Р-К четвертого порядка')
    pl.legend()


def prediction_and_correction(h, n, x0, y0):
    x = np.empty(n)
    y = np.empty(n)
    x[0] = x0
    y[0] = y0
    i = 0
    while i < n-1:
        prediction = y[i] + (h ** 2) * f(x[i], y[i])
        y[i + 1] = y[i] + h * f(x[i], y[i]) + (f(x[i] + h ** 2, prediction) - f(x[i], y[i])) / 2
        x[i + 1] = x[i] + h
        i += 1
    g = np.linspace(x[0], x[-1], 100)
    d = np.linspace(y[0], y[-1], 100)
    pl.plot(g, d, 'g--', label=u'Метод прогноза и коррекции')
    pl.legend()


def run():
    h = 0.1
    n = 4

    x0 = 0
    y0 = 2

    runge_kutta_3(h, n, x0, y0)
    runge_kutta_4(h, n, x0, y0)
    prediction_and_correction(h, n, x0, y0)
    pl.grid()
    pl.show()


if __name__ == '__main__':
    run()
