# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


def fun1(a, b):
    print('a+b=', a + b)  # вывод на экран операция сложение


def fun2(a, b):
    print('a/b=', a / b)  # вывод на экран операция деление


def fun3(a, b):
    print('a*b=', a * b)  # вывод на экран операция умножение


def fun4(a, b):
    print('a%b=', a % b)  # вывод на экран операция деление по модулю


def fun5(a, b):
    print('a//b=', a // b)  # вывод на экран целочисленное деление


def fun6(a, b):
    print('a**b=', a ** b)  # вывод на экран операция возведение в степень


def fun7(a, b):
    print('a-b=', a - b)  # вывод на экран операция вычитание


def fun8(a, b):
    print('0-звершение работы')  # вывод на экран операция возведение в степень


def fun9(a, b):
    print('На 0 делить нельзя. Повторите ввод')


while True:
    a = float(input('введите число a '))  # Запрос пользователя ввести первое любое число
    b = float(input('введите число b '))  # Запрос пользователя ввести второе целое число
    s = input("Введите действие над числами +,-,/,*,%,//,**, 0 - выход: ")
    if b == 0 and s == '/' or s == '//':
        fun9(a, b)
        continue
    if s == '+':
        fun1(a, b)
    elif s == '/':
        fun2(a, b)
    elif s == '*':
        fun3(a, b)
    elif s == '%':
        fun4(a, b)
    elif s == '//':
        fun5(a, b)
    elif s == '**':
        fun6(a, b)
    elif s == '-':
        fun7(a, b)
    elif s == '0':
        fun8(a, b)
        break
    else:
        print('не верное значение повторите ввод')
