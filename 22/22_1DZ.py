# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

# =====================================================
class calculator:

    def __init__(self, a, b):

        self.a = a
        self.b = b

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

    def cal(self):

        if s == "+":
            print('a+b=', obj.plus(self.a, self.b))
        if s == "-":
            print('a-b=', obj.minus(self.a, self.b))
        if s == "*":
            print('a*b', obj.proisv(self.a, self.b))
        if s == "/":
            print('a/b=', obj.delen(self.a, self.b))
        if s == "//":
            print('a//=', obj.fun1(self.a, self.b))
        if s == '%':
            print('a%b=', obj.fun2(self.a, self.b))
        if s == '**':
            print('a**b=', obj.fun3(self.a, self.b))


# =============================================================================
while True:
    try:
        print('_________Калькулятор:__________')
        obj = calculator(a=float(input('введите число a ')),
                         b=float(input('введите число b ')))
        s = input("Введите действие над числами +,-,/,*,%,//,**, 0 - выход: ")
        obj.cal()
        if s == '0':
            obj.vix()
            break
    except ValueError:
        print('!!!!_____ERROR......Что-то пошло не так______!!!!!')

# =====================================================================================
