from Functions import task_one_function as f


# Вычисляет f(x)=0 методом половинного деления
def compute(a, b, eps):
    c = (a + b) / 2
    i = 0
    while abs(a - b) > eps:
        i += 1
        if f.value(c) == 0:
            return c
        elif f.value(a) * f.value(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0
    return c, i
