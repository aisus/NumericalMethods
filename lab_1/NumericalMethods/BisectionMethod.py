# Вычисляет f(x)=0 методом половинного деления
def compute(f, a, b, eps):
    c = (a+b) / 2
    while abs(a-b) > eps or f.value(c) > eps:
        if f.value(c) == 0:
            return c
        elif f.value(a) * f.value(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0
    return c