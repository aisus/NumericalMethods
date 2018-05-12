from labs.src.lab_1.numerical_methods import bisection_method, secant_method
from labs.src.lab_1.functions import task_one_function as f
import matplotlib.pyplot as pyplot

# Параметры графика
plot_left_border = -4
plot_right_border = 4
plot_points_count = 100

# Значение точности - степень 10
eps_power_of_ten = -4


def run():
    while True:

        print('_________________________________________')

        create_plot(plot_left_border, plot_right_border, plot_points_count)

        print('Введите параметры для метода половинного деления:')
        xa = float(input("    Начальное приближение слева: "))
        xb = float(input("    Начальное приближение справа: "))

        print('Введите параметры для метода секущих:')
        x0 = float(input("    Первое приближение: "))

        print('Метод половинного деления')
        x, i = bisection_method.compute(xa, xb, 10 ** eps_power_of_ten)

        print('    Результат: x =', round(x, abs(eps_power_of_ten) + 1))
        # print('    Невязка: ', round(abs(f.value(x)), abs(eps_power_of_ten) + 1))
        print('    Невязка: {:.2e}'.format(abs(f.value(x))))
        print('    Число итераций: ', i)

        print('Метод секущих')
        x, i = secant_method.compute(x0, 10 ** eps_power_of_ten)

        print('    Результат: x =', round(x, abs(eps_power_of_ten) + 1))
        # print('    Невязка: ', round(abs(f.value(x)), abs(eps_power_of_ten) + 1))
        print('    Невязка: {:.2e}'.format(abs(f.value(x))))
        print('    Число итераций: ', i)

        ans = input('Завершить работу? (y/n) ')
        if ans == 'y':
            break


def create_plot(x0, xn, n):
    x = []
    y = []

    step = (xn - x0) / n
    while x0 < xn:
        x.append(x0)
        y.append(f.value(x0))
        x0 += step

    # Сама функция
    pyplot.plot(x, y, 'b')

    # Линия y=0
    pyplot.plot([x[0], x[-1]], [0, 0], 'gray')

    pyplot.axis([x[0], x[-1], min(y), max(y)])
    pyplot.ylabel('y')
    pyplot.xlabel('x')
    pyplot.show()


if __name__ == '__main__':
    run()
