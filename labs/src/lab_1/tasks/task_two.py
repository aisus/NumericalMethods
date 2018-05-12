import math

from labs.src.lab_1.functions import task_two_functions as f
from labs.src.lab_1.numerical_methods import newton_method_system
import matplotlib.pyplot as pyplot

# Параметры графика
plot_left_border = -2
plot_right_border = 2
plot_points_count = 100

# Значение точности - степень 10
eps_power_of_ten = -5


def run():
    print('Методы Ньютона для системы')
    while True:

        print('_________________________________________')

        create_plot(plot_left_border, plot_right_border, plot_points_count)

        print('Введите параметры:')
        x0 = float(input("    Начальное приближение, x: "))
        y0 = float(input("    Начальное приближение, y: "))

        print('Стандартный метод Ньютона:')
        x, i = newton_method_system.compute_standart(x0, y0, 10 ** eps_power_of_ten)

        print('    Результат: x,y =', x)
        print('    Невязка: {:.2e}'.format(abs(f.value(x)[0] - f.value(x)[1])))
        print('    Число итераций: ', i)

        print('Модифицированный метод Ньютона:')
        x, i = newton_method_system.compute_modified(x0, y0, 10 ** eps_power_of_ten)

        print('    Результат: x,y =', x)
        print('    Невязка: {:.2e}'.format(abs(f.value(x)[0] - f.value(x)[1])))
        print('    Число итераций: ', i)

        ans = input('Завершить работу? (y/n) ')
        if ans == 'y':
            break


def create_plot(x0, xn, n):
    x = []
    y0 = []
    y1 = []

    step = (xn - x0) / n
    while x0 < xn:
        x.append(x0)
        y0.append(math.sin(x0+0.5)-1)
        y1.append(-math.cos(x0-2))
        x0 += step

    # Первая функция
    pyplot.plot(x, y0, 'b')

    # Вторая функция
    pyplot.plot(x, y1, 'g')

    # Линия y=0
    pyplot.plot([x[0], x[-1]], [0, 0], 'gray')

    pyplot.axis([x[0], x[-1], min(y0), max(y1)])
    pyplot.ylabel('y')
    pyplot.xlabel('x')
    pyplot.show()


if __name__ == '__main__':
    run()
