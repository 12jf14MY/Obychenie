# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

# =====================================================
class calculator:

    def vvod(self):
        global a, b, s
        print('_________Калькулятор:__________')
        a = float(input('введите число a '))
        b = float(input('введите число b '))
        s = input("Введите действие над числами +,-,/,*,%,//,**, 0 - выход: ")

    def delen(self, a, b):
        if b == 0:
            return "error.... На 0 делить нельзя. Повторите ввод"
        else:
            return a / b

    def fun1(self, a, b):
        if b == 0:
            return "error.... На 0 делить нельзя. Повторите ввод"
        else:
            return a // b

    def fun2(self, a, b):
        return a % b

    def fun3(self, a, b):
        return a ** b

    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def proisv(self, a, b):
        return a * b

    def vix(self):
        print('<<<<<<ЗАВЕРШЕНИЕ РАБОТЫ>>>>>>>')


class operation():

    def cal(self):

        if s == "+":
            print('a+b=', obj.plus(a, b))
        if s == "-":
            print('a-b=', obj.minus(a, b))
        if s == "*":
            print('a*b', obj.proisv(a, b))
        if s == "/":
            print('a/b=', obj.delen(a, b))
        if s == "//":
            print('a//=', obj.fun1(a, b))
        if s == '%':
            print('a%b=', obj.fun2(a, b))
        if s == '**':
            print('a**b=', obj.fun3(a, b))


# =============================================================================
while True:
    try:
        obj = calculator()
        obj_1 = operation()
        obj.vvod()
        obj_1.cal()
        if s == '0':
            obj.vix()
            break
    except ValueError:
        print('!!!!_____ERROR......Что-то пошло не так______!!!!!')

# =====================================================================================