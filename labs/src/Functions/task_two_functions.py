import math
import numpy as np


def value(x):
    return [math.sin(x[0] + 0.5) - x[1] - 1, x[0] + math.cos(x[1] - 2)]


def inverted_jacobi_matrix(x):
    res = np.zeros((2, 2))

    # [d -b]
    # [-c a]
    res[0, 0] = -math.sin(x[1] - 2)
    res[0, 1] = 1
    res[1, 0] = -1
    res[1, 1] = math.cos(x[0] + 0.5)

    det = res[0, 0] * res[1, 1] - res[0, 1] * res[1, 0]

    res /= det
    return res
