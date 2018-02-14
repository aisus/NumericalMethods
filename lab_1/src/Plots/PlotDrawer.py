import matplotlib.pyplot as plot_drawer


# Рисует график
def createPlot(f):

    x = []
    y = []

    for point in f.points:
        x.append(point.x)
        y.append(point.y)

    # Сама функция
    plot_drawer.plot(x, y, 'b')

    # Линия y=0
    # TODO должны быть встроенные функции для рисования осей, найти
    plot_drawer.plot([x[0], x[-1]], [0, 0], 'gray')

    plot_drawer.axis([x[0], x[-1], min(y), max(y)])
    plot_drawer.ylabel('y')
    plot_drawer.xlabel('x')
    plot_drawer.show()
