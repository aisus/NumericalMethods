import numpy as np
import math as m
from matplotlib import pyplot as pl


def f(x):
    return m.exp(3 * x) / ((x ** 3) + m.sqrt(x + 1))


def source_function_plot(a, b, n):
    pl.figure("Source function")

    x = np.linspace(a, b, n)
    y = []
    step = (b - a) / n

    for i in range(n):
        y.append(f(a + i * step))

    pl.plot(x, y, 'purple', label='source function')
    pl.legend()
    pl.grid()
    pl.show()


def trapezoidal_integration(a, b, n):
    h = (b - a) / n
    res = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        res += f(a + i * h)
    return h * res


def trapezoidal_integration_with_precision(a, b, eps):
    n = 0
    prev_res = float('inf')
    res = 0
    while abs(prev_res - res) > eps:
        n += 1
        prev_res = res
        res = trapezoidal_integration(a, b, n)
    # print('Trap. integration for eps=', eps, 'completed with', n, 'iterations')
    return res


def simpson_integration(a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(0, n, 2):
        res += 2 * f(a + i * h)
    for i in range(1, n, 2):
        res += 4 * f(a + i * h)
    return h * res / 3


def run():
    a = 2
    b = 3
    eps = 10 ** -5
    n = 10

    source_function_plot(a, b, n)
    print('Trap. result:', trapezoidal_integration_with_precision(a, b, eps))
    print('Simpson result:', simpson_integration(a, b, n))


if __name__ == '__main__':
    run()
