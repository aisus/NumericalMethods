from Functions import Functions
from Plots import PlotDrawer
from NumericalMethods import BisectionMethod


def run():
    f = Functions.FirstTaskFunction(-4, 4, 100)

    print('Метод половинного деления')
    # TODO вытащить в функцию
    while True:
        PlotDrawer.createPlot(f)

        a = float(input("Левая граница: "))
        b = float(input("Правая граница: "))

        x = BisectionMethod.compute(f, a, b, 0.001)

        print('Результат: x=', x)
        print('Невязка: ', abs(f.value(x)))

        ans = input('Завершить работу? (y/n) ')
        if ans == 'y':
            break

    # TODO здесь повторить процедуру для метода секущих


if __name__ == '__main__':
    run()
