# Вычисляет f(x)=0 методом секущих
def compute(f, x0, x1, eps):
    i = 0
    while abs(x1 - x0) > eps:
        x2 = x1 - ((x1 - x0) / (f.value(x1) - f.value(x0))) * f.value(x1)
        x0 = x1
        x1 = x2
        i += 1
    return x1, i
