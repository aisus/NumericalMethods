from Functions import functions
from Plots import plot_drawer
from NumericalMethods import bisection_method
from NumericalMethods import secant_method

# Параметры графика
plot_left_border = -4
plot_right_border = 4
plot_points_count = 100

# Значение точности - степень 10
eps_power_of_ten = -4


def run():
    while True:

        print('_________________________________________')
        f = functions.FirstTaskFunction()

        plot_drawer.create_plot(f, plot_left_border, plot_right_border, plot_points_count)

        print('Параметры:')
        xa = float(input("    Начальное приближение слева: "))
        xb = float(input("    Начальное приближение справа: "))

        print('Метод половинного деления')
        x, i = bisection_method.compute(f, xa, xb, 10 ** eps_power_of_ten)

        print('    Результат: x =', round(x, abs(eps_power_of_ten)+1))
        print('    Невязка: ', round(abs(f.value(x)), abs(eps_power_of_ten)+1))
        print('    Число итераций: ', i)

        print('Метод секущих')
        x, i = secant_method.compute(f, xa, xb, 10 ** eps_power_of_ten)
        print('    Результат: x =', round(x, abs(eps_power_of_ten) + 1))
        print('    Невязка: ', round(abs(f.value(x)), abs(eps_power_of_ten) + 1))
        print('    Число итераций: ', i)

        ans = input('Завершить работу? (y/n) ')
        if ans == 'y':
            break


if __name__ == '__main__':
    run()
