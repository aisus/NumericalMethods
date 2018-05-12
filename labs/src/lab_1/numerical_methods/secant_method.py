from labs.src.lab_1.functions import task_one_function as f


# Вычисляет f(x)=0 методом секущих
def compute(x0, eps):
    i = 0
    x1 = x0 - 2*eps
    while abs(x1 - x0) > eps:
        x2 = x1 - ((x1 - x0) / (f.value(x1) - f.value(x0))) * f.value(x1)
        x0 = x1
        x1 = x2
        i += 1
    return x1, i
