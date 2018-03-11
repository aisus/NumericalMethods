import numpy as np
from Functions import task_two_functions as f


# Решает систему методом Ньютона
def compute(x0, y0, eps):
    i = 0
    xk = [x0, y0]
    while True:

        i += 1

        fxk = f.value(xk)
        jacoby_inv = f.inverted_jacobi_matrix(xk)

        tmp = np.dot(jacoby_inv, np.matrix([[fxk[0]], [fxk[1]]]))
        xk1 = np.subtract(xk, [tmp[0, 0], tmp[1, 0]])

        norm = np.linalg.norm(np.subtract(xk1, xk))

        if norm < eps:
            return xk1, i

        xk = xk1
