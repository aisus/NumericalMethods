import math
import numpy as np


def value(x):
    return [math.sin(x + 0.5) - 1, -math.cos(x - 2)]


def inverted_jacobi_matrix(x):
    res = np.zeros((2, 2))

    # [a b]
    # [c d]
    res[0, 0] = math.cos(x + 0.5)
    res[0, 1] = -1
    res[1, 0] = 1
    res[1, 1] = -math.sin(x - 2)

    det = res[0, 0] * res[1, 1] - res[0, 1] * res[1, 0]

    # [d -b]
    # [-c a]
    tmp = res[0, 0]
    res[0, 0] = res[1, 1]
    res[1, 1] = tmp
    res[0, 1] *= -1
    res[1, 0] *= -1

    res /= det
    return res

