import numpy as np
import math as m


def f(x):
    return m.exp(3 * x) / x ** 3 + m.sqrt(x + 1)


def trapezoidal_integration(a, b, n):
    h = (b-a)/n
    s = 0.5*(f(a)+f(b))
    for i in range(1, n, 1):
        s = s + f(a + i * h)
    return h * s

def run():
    a = 2
    b = 3
    eps = 10 ** -5
    n = 100

    print(trapezoidal_integration(a, b, n))


if __name__ == '__main__':
    run()
