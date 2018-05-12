import math
import numpy as np
from matplotlib import pyplot as pl


def f(x):
    return 8 * math.pi * (12 + math.pi * x) ** 0.5
    # return x / 10 * math.pi * math.sin(x)
    # return x


def dx4_max(x):
    return abs((-15 * math.pi ** 5) / (2 * ((math.pi * x + 12) ** (7 / 2)))) / 24


def finite2(x0, x1):
    return (f(x1) - f(x0)) / (x1 - x0)


def finite3(x0, x1, x2):
    return (finite2(x1, x2) - finite2(x0, x1)) / (x2 - x0)


def finite4(x0, x1, x2, x3):
    return (finite3(x1, x2, x3) - finite3(x0, x1, x2)) / (x3 - x0)


def step(a, b):  # находим шаг (параметры - какой нибудь начальный отрезок)

    def maxfunc(x_, x0, h):  # |w_n+1|
        return abs((x_ - x0) * (x_ - x0 - h) * (x_ - x0 - 2 * h) * (x_ - x0 - 3 * h))

    def maxW_n_1(a, b, h):  # метод золотого сечения для поиска максимума
        PHI = (np.sqrt(5) + 1) / 2
        while abs(b - a) >= 0.00001:
            x2 = a + (b - a) / PHI
            x1 = b - (b - a) / PHI

            if abs(maxfunc(x1, x0, h)) <= (abs(maxfunc(x2, x0, h))):
                a = x1
            else:
                if abs((maxfunc(x1, x0, h))) > (abs(maxfunc(x2, x0, h))):
                    b = x2
        return (a + b) / 2

    x3 = b  # правая граница
    x0 = a  # левая граница
    h = (x3 - x0) / 3  # шаг
    R3 = 1  # погрешность
    x_ = maxW_n_1(x0, x3, h)  # max x_ для |w_n+1|

    max = dx4_max(b)  # само max |w_n+1|

    while abs(R3 / f(x_)) > 10 ** -3:
        R3 = (max * (x_ - x0) * (x_ - x0 - h) * (x_ - x0 - 2 * h) * (x_ - x0 - 3 * h))
        x0 = x0 + 0.01
        h = (x3 - x0) / 3
        x_ = maxW_n_1(x0, x3, h)

    # print("x0 = ", x0, "R3 = ", abs((R3 / f(x_))), "h  =", h)
    return x0, h


def tabulated_function_values(a, b, h, xarr, out):
    x = a

    while x <= b:
        out.append(f(x))
        xarr.append(x)
        x += h


def poly_plot(a, b, source, lag, newt):
    pl.figure("Polynomials")
    pl.plot(np.linspace(a, b, len(source)), source, 'b', label='f(x)')
    pl.plot(np.linspace(a, b, len(lag)), lag, 'r', label='lagrange')
    pl.plot(np.linspace(a, b, len(newt)), newt, 'g', label='newton')
    pl.grid()
    pl.legend()
    pl.show()


def spline_plot(a, b, source, lin_sp, par_sp, cub_sp):
    pl.figure("Splines")
    pl.plot(np.linspace(a, b, len(source)), source, 'b', label='f(x)')
    pl.plot(lin_sp[0], lin_sp[1], 'purple', label='linear spline')
    pl.plot(par_sp[0], par_sp[1], 'g', label='parabolic spline')
    pl.plot(cub_sp[0], cub_sp[1], 'gray', label='cubic spline')
    pl.grid()
    pl.legend()
    pl.show()


def error_plot(lag, newt, lin, par, cub):
    pl.figure("Errors")
    pl.plot(lag[0], lag[1], 'purple', label='lagrange')
    pl.plot(newt[0], newt[1], 'g', label='newton')
    pl.plot(lin[0], lin[1], 'b', label='linear spline')
    pl.plot(par[0], par[1], 'r', label='parabolic spline')
    pl.plot(cub[0], cub[1], 'gray', label='cubic spline')
    pl.grid()
    pl.legend()
    pl.show()


def lagrange(x, x_arr):
    n = len(x_arr)
    res = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if i == j:
                continue
            l *= (x - x_arr[j]) / (x_arr[i] - x_arr[j])
        res += f(x_arr[i]) * l
    return res


def newton(x, x_arr):
    return f(x_arr[0]) + finite2(x_arr[0], x_arr[1]) * (x - x_arr[0]) + finite3(x_arr[0], x_arr[1], x_arr[2]) * (
            x - x_arr[0]) * (
                   x - x_arr[1]) + finite4(x_arr[0], x_arr[1], x_arr[2], x_arr[3]) * (x - x_arr[0]) * (x - x_arr[1]) * (
                   x - x_arr[2])


def linearSpline(x, y, h,
                 delt):  # параметры - (массивы х,у ,шаг исходный, шаг для оценки погрешности(гораздо меньше чем исходный))
    A = [[1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [1, h, 0, 0, 0, 0],
         [0, 0, 1, h, 0, 0],
         [0, 0, 0, 0, 1, h]]

    b = [[y[0]], [y[1]], [y[2]], [y[1]], [y[2]], [y[3]]]

    ans = np.linalg.solve(A, b)
    X = x[0]
    ansY = []
    ansX = []

    while X < x[1]:
        ansY.append(ans[0] + ans[1] * (X - x[0]))
        ansX.append(X)
        X = X + delt

    while X < x[2]:
        ansY.append(ans[2] + ans[3] * (X - x[1]))
        ansX.append(X)
        X = X + delt

    while X <= x[3]:
        ansY.append(ans[4] + ans[5] * (X - x[2]))
        ansX.append(X)
        X = X + delt

    return ansX, ansY


def parabolSpline(x, y, h, delt):  # аналогично линейному
    A = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, h, h ** 2, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, h, h ** 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, h, h ** 2],
         [0, 1, 2 * h, 0, -1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 2 * h, 0, -1, 0],
         [0, 0, 2, 0, 0, 0, 0, 0, 0]]

    b = [[y[0]], [y[1]], [y[2]], [y[1]], [y[2]], [y[3]], [0], [0], [0]]

    ans = np.linalg.solve(A, b)
    X = x[0]
    ansY = []
    ansX = []

    while X < x[1]:
        ansY.append(ans[0] + ans[1] * (X - x[0]) + ans[2] * (X - x[0]) ** 2)
        ansX.append(X)
        X = X + delt

    while X < x[2]:
        ansY.append(ans[3] + ans[4] * (X - x[1]) + ans[5] * (X - x[1]) ** 2)
        ansX.append(X)
        X = X + delt

    while X <= x[3]:
        ansY.append(ans[6] + ans[7] * (X - x[2]) + ans[8] * (X - x[2]) ** 2)
        ansX.append(X)
        X = X + delt

    return ansX, ansY


def cubSpline(x, y, h, delt):  # аналогично линейному
    A = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, h, h ** 2, h ** 3, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, h, h ** 2, h ** 3, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, h, h ** 2, h ** 3],
         [0, 1, 2 * h, 3 * h ** 2, 0, -1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 2 * h, 3 * h ** 2, 0, -1, 0, 0],
         [0, 0, 1, 3 * h, 0, 0, -1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 3 * h, 0, 0, -1, 0],
         [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3 * h]]

    b = [[y[0]], [y[1]], [y[2]], [y[1]], [y[2]], [y[3]], [0], [0], [0], [0], [0], [0]]

    ans = np.linalg.solve(A, b)
    X = x[0]
    ansY = []
    ansX = []
    while X < x[1]:
        ansY.append(ans[0] + ans[1] * (X - x[0]) + ans[2] * (X - x[0]) ** 2 + ans[3] * (X - x[0]) ** 3)
        ansX.append(X)
        X = X + delt

    while X < x[2]:
        ansY.append(ans[4] + ans[5] * (X - x[1]) + ans[6] * (X - x[1]) ** 2 + ans[7] * (X - x[1]) ** 3)
        ansX.append(X)
        X = X + delt

    while X <= x[3]:
        ansY.append(ans[8] + ans[9] * (X - x[2]) + ans[10] * (X - x[2]) ** 2 + ans[11] * (X - x[2]) ** 3)
        ansX.append(X)
        X = X + delt

    return ansX, ansY


def newton_error(x):
    x_err = []
    y_err = []
    xi = x[0]
    while xi <= x[3]:
        y_err.append(abs(f(xi) - newton(xi, x)))
        x_err.append(xi)
        xi = xi + 0.008

    return x_err, y_err


def lagrange_error(x):
    x_err = []
    y_err = []
    xi = x[0]
    while xi <= x[3]:
        y_err.append(abs(f(xi) - lagrange(xi, x)))
        x_err.append(xi)
        xi = xi + 0.006

    return x_err, y_err


def spline_error(x, spline_xy):
    x_err = []
    y_err = []
    for i in range(0, len(spline_xy[0])):
        y_err.append(abs(f(spline_xy[0][i]) - spline_xy[1][i]))
        x_err.append(spline_xy[0][i])

    return x_err, y_err


def run():
    a = 0
    b = 3.5

    temp = step(a, b)

    a = temp[0]
    h = temp[1]

    x = []
    y = []

    tabulated_function_values(a, b, h, x, y)

    newt = []
    lag = []

    gg = x[0]
    ggx = []
    while gg <= x[3]:
        lag.append(lagrange(gg, x))
        newt.append(newton(gg, x))
        ggx.append(gg)
        gg += 0.001

    X_Y_parabol_sp = parabolSpline(x, y, h, 0.001)
    X_Y_cub_sp = cubSpline(x, y, h, 0.001)
    X_Y_lin_sp = linearSpline(x, y, h, 0.001)

    poly_plot(x[0], x[-1], y, lag, newt)
    spline_plot(x[0], x[-1], y, X_Y_lin_sp, X_Y_parabol_sp, X_Y_cub_sp)

    error_lagrange = lagrange_error(x)
    error_newton = newton_error(x)
    error_lin = spline_error(x, X_Y_lin_sp)
    error_parab = spline_error(x, X_Y_parabol_sp)
    error_cub = spline_error(x, X_Y_cub_sp)

    error_plot(error_lagrange, error_newton, error_lin, error_parab, error_cub)


if __name__ == '__main__':
    run()
