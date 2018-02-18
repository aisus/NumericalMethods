import matplotlib.pyplot as plot_drawer


# Рисует график
def create_plot(f, x0, xn, n):

    x = []
    y = []

    step = (xn - x0) / n
    while x0 < xn:
        x.append(x0)
        y.append(f.value(x0))
        x0 += step

    # Сама функция
    plot_drawer.plot(x, y, 'b')

    # Линия y=0
    # TODO должны быть встроенные функции для рисования осей, найти
    plot_drawer.plot([x[0], x[-1]], [0, 0], 'gray')

    plot_drawer.axis([x[0], x[-1], min(y), max(y)])
    plot_drawer.ylabel('y')
    plot_drawer.xlabel('x')
    plot_drawer.show()
