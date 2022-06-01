# Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для работы с числами.
math.acos(X)  # - арккосинус X. В радианах
math.pow(X, Y)  # - XY.
math.asin(X)  # - арксинус X. В радианах.
math.atan(X)  # - арктангенс X. В радианах.
math.cos(X)  # - косинус X (X указывается в радианах).
math.sin(X)  # - синус X (X указывается в радианах).
math.tan(X)  # - тангенс X (X указывается в радианах).
math.factorial(X)  # - факториал числа X.
math.floor(X)  # - округление вниз.
math.ceil(X)  # – округление до ближайшего большего числа.
math.sqrt(X)  # - квадратный корень из X.
math.fabs(X)  # - модуль X.

# модуль random
random.randint(A, B)  # - #случайное целое число N, A ≤ N ≤ B.
random.uniform(A, B)  # - случайное число с плавающей точкой, A ≤ N ≤ B.
random.random()  # - случайное число от 0 до 1.
random.choice(sequence)  # - случайный элемент непустой последовательности.

print(i, end='') -  # вывод знвчения в строку для цикла
# Делаем строку заголовком
print(s.title())
# Начинаем строку с заглавной буквы
print(s.capitalize())
# Переводим строку в верхний регистр
print(s.upper())
# Переводим строку в нижний регистр
print(s.lower())
# Инверсия регистра
print(s_2.swapcase())
# Возвращает True, если все символы строки, поддерживающие приведение к регистру, приведены к верхнему, иначе — False.
s.isupper()
# Возвращает True, если все символы строки, поддерживающие приведение к регистру, приведены к нижнему, иначе — False.
s.islower()
# Определяет, начинаются ли слова строки с заглавной буквы. Возвращает True, когда s не пустая строка и первый алфавитный символ каждого слова в верхнем регистре, а все остальные буквенные символы в каждом слове строчные. Иначе - False.
s.istitle()

S.isdigit()  # -  Состоит ли строка из цифр.
S.isalpha()  # -  Состоит ли строка из букв.

# Возвращает строку, собранную из элементов указанного объекта, поддерживающего итерирование(например, список строк).
x.join(iterable) # список в строку пример c = " ".join(b)
# Разбивает строку s на части, используя специальный разделитель x, и возвращает эти части в виде списка
s.split(x) # строка в список пример b = a.split(' ')

# Возвращает True, если строка s начинается с указанного префикса, иначе - False.
s.startswith(prefix)

# Возвращает True, если строка s оканчивается указанным постфиксом, иначе - False.
s.endswith(suffix)

# Находит в строке s подстроку sub. Возвращает индекс первого вхождения искомой подстроки. Если же подстрока не найдена, то метод возвращает значение -1.
s.find(sub)

# Заменяет в строке s все вхождения подстроки old на подстроку new.
s.replace(old, new)

find()  # поиск подстроки, вернет -1 если не найдет
index()  # поиск индекса, выдаст ошибку если не найдет

# что если нужно только удостовериться, что подстрока присутствует внутри строки - можно просто воспользоваться методом in:'Py' in 'Python’  # True
in

range(4, 8)  # - формирует диапазон от 4 до 8, не включая 8 = (4,5,6,7)
range(4, 8, 1)  # - 1 - это шаг, шаг может быть и отрицательным.

a.append(х)  # - добавление элемента в конец массива илм списка .
a.count(х)  # - возвращает количество вхождений х в массив.
a.index(х)  # - номер первого индекса x в массив.
a.pop(i)  # - удаляет i-ый элемент из массива и возвращает его. По умолчанию удаляется последний элемент.
a.remove(х)  # - удалить первое вхождение х из массива.
a.reverse(x)  # - обратный порядок элементов в массиве.

# Списки
list.insert(i, x)  # , где list – список, i – позиция, x – нужное значение.

del list[i]  # Для удаление из списка используют инструкцию  где list – список, i – индекс (позиция) элемента в списке.
list.remove(
    x)  # Еще один способ удаления из списка – list.remove(x) , где list – список, x – значение, которое нужно удалить.
list.pop(i)  # - удалит элемент из позиции i ;

a.extend(b)  # к списку а дополняет b

# Для копирования списков можно использовать несколько вариантов:

a.copy()  # – встроенный метод copy (доступен с Python 3.3);
list(a)  # – через встроенную функцию list() ;
copy.copy(a)  # – функция copy() из пакета copy;
a[:]  # – через создание среза (устаревший синтаксис);

# методы списков
list.append(x)  # – позволяет добавлять элемент в конец списка; не работает с множеством
list1.extend(list2)  # – предназначен для сложения списков;
list.insert(i, x)  # – служит для добавления элемента на указанную позицию( i – позиция, x – элемент);
list.remove(x)  # – удаляет элемент из списка (только первое вхождение);
list.clear()  # – предназначен для удаления всех элементов (после этой операции список становится пустым []);
list.copy()  # – служит для копирования списков.
list.count(x)  # – посчитает количество элементов x в списке;
list.index(x)  # – вернет позицию первого найденного элемента x в списке;
A.index(min(A))+1) - #  Вывести на экран порядковые номера минимальных элементов
list.pop(i)  # - удалит элемент из позиции i ;
list.reverse()  # – меняет порядок элементов в списке на противоположный;
list.sort()  # – сортирует список;
list.sort(key=len)  # сортировка по количеству символов
b.sort(reverse=True)  # сортировка в обратном порядке





type(i)  # тип переменной i
print(type(i))  # так можно проверить тип  i
print(b.__sizeof__())  # объем (мб) занимаемый списком или кортежем

a = tuple()  # Создание кортежа ()
b = list()  # создание списка []
c = dict()  # создание словаря {}
d = set()  # Создание множества {}

# максимальное и мин число в кортеже
print(max(a))  # к спискам[] тоже применяется
print(min(a))  # к спискам[] тоже применяется
print(sum(a))  # к спискам[] тоже применяется

print(max(a, key=len))  # к спискам[] тоже применяется a=('jhdsf','gjh','husd','ss') самый длинная строка в кортедже
print(min(a, key=len))  # к спискам[] тоже применяется a=('jhdsf','gjh','husd','ss') самая короткая строка в кортеже

# СОЗДАНИЕ СЛОВАРЕЙ
f = dict(zip([1, 2, 3], ['one', 'two', 'three']))  # создание словаря из 2х списков
d = {}  # создание словаря через литерал
d = dict(short='dict', long='dictionary')  # цифры ключом быть не могут.
d_2 = dict([(1, 1), (2, 4)])  # ограничений нет
d = dict.fromkeys(['a', 'b'], 100)  # с помощью метода fromkeys
# с помощью генераторов словарей
d = {a: a ** 2 for a in range(7)}
d = {a: random.randint(1, 10) for a in ['a', 'b']}

Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals = dict(Russia='Moscow', Ukraine='Kiev', USA='Washington')
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))

del d[5]  # Операция del - удаление элемента из словаря

dict.clear()  # - очищает словарь. и работает при множестве
dict.copy()  # - возвращает копию словаря.
dict.items()  # - возвращает пары (ключ, значение).
dict.keys()  # - возвращает ключи в словаре.
dict.pop(key[,
         default])  # - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
dict.values()  # - возвращает значения в словаре.
стандартный
метод
len(dict)  # – определяет количество элементов в списке.

a = key in D  # Определение наличия ключа в словаре
a = key not in D  # Определение отсутствия ключа в словаре

# Множество

c = set()  # Создание множества
a = frozenset([1, 4, 'rete', 34, ])  # создание замороженного множества

a.discard(
    5)  # удаление элемента множества, если есть ошибка т.е. нет элемента во множестве но прога продолжает работать
a.remove(9)  # удаление элемента множества, но выдает ошибку и завершает работу
x = a.pop()  # удаление из позиции

f = a.union(b, c)  # объединение множеств a и b и с
print(x | y | z)  # объединение множеств (только у множеств)
# &-амперсант
print(x & z)  # пересечение множеств. т.е. одинаковые элементы в 2х множествах
print(z - x)  # разница множест
print(x - z)  # разница множест
t = z.copy()  # копирование множеств
p = x.isdisjoint(
    z)  # проверка множества является ли пересечением. если множества не содержат общие элементы то True. Содержит false
a = frozenset([1, 4, 'rete', 34, ])  # создание замороженного множества
a.add('33333333')  # добавление во множество

# ИСКЛЮЧЕНИЯ
# обработка ошибки деления на 0
try:
    a = 100 / 0
except ZeroDivisionError:
    a = 0

# обработка нескольких ошибок
dict = {'a': 1, 'b': 2, 'c': 3}
try:
    value = dict['d']
except KeyError:
    print(' ключа не существует')
except IndexError:
    print(' этого индекса нет в списке')
except:
    print('произошла другая ошибка')
finally:  # применяется если нужно что то обязательно сделать, например закрыть файл
    print('оепратор finally выполнен ')
else:
print('ошибок не возникло')

# BaseException - базовое исключение, от которого берут начало все остальные.
# 	SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
# 	KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
# 	Exception – то, на чем фактически строятся все остальные ошибки;
# 		StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
# 		ArithmeticError - арифметическая ошибка.
# 			FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой.
# 			На практике встречается нечасто.
# 			OverflowError - возникает, когда результат арифметической операции 	слишком велик для представления.
# 			Не появляется при обычной работе с 				целыми числами (так как python поддерживает длинные числа),
# 			но может 				возникать в некоторых других случаях.
# 			ZeroDivisionError - деление на ноль.
# #


# ФАЙЛЫ

f = open('1.txt', 'r', encoding='utf-8')  # открытие файля 1. txt для чтения encoding='utf-8'- для вывода русских букв
f.close()  # закрытие файла

# ПРИМЕРЫ РАБОТЫ С ФАЙЛАМИ
# пример с finally
f = open('1.txt', 'r', encoding='utf-8')
try:
    print(*f)  # либо другая работа с файлом
finally:
    f.close()

# пример с with - as в конце файл автоматом закрывается
with open('1.txt', 'r', encoding='utf-8') as f:
    print(*f)
file.read(size) # size = количество символов, которые нужно прочитать. Если не указать, то файл прочитается целиком.
f.read()

f.readline()  # читает по 1 строке
f.readlines()  # читает все строки сразу
f.write('shfksdhfsdhkj') - # запись в открытый файл f



import os # ввод новой функции для работы с файлами

print('текущая директория', os.getcwd())  # показывает путь где работаем
os.rename('2.txt', 'twxt.txt')  # переименовывает 2 в twxt.txt
os.mkdir('folser')  # создание папки
os.chdir('folder') # смена директории
os.chdir('..') # возврат в предыдущую директорию выше директории
os.makedirs('n1/n2/n3') # создание входящих папок (каскадом дерево) в директорию
os.remove('folder/2.txt') # удаляет файл 2 в папке folder
os.rmdir('folder')  # удаление пустой папки. обязательно пустой!!!
os.removedirs('n1/n2/n3') # удалЯет папки каскадом все дерево


with open('2.txt', 'w', encoding='utf-8') as f:  # создаем файл 2 в текущей директории
    # ('w'- создает новый файл если не находит с этим именнем)
    f.write('hello \nWorld')  # записываем в файл 2
    f.write(line + '\n') # запись по строкам



# Git это система контроля версий

для регистрации
git config --global user.name "yury"
git config --global user.email "y.maiseyonak@gmail.com"
git init - создание локальный репозиторий
git status - посмотреть какой статус работы
git add . - отслеживает файлы
git add <имя файла>  - добавляет конкретный файл
git commit -m "test1" - коммитим(сохраняем) с названием test1
git log - вывести все коммиты

git branch -a   # посмотреть список всех веток
git checkout master — переходим на ветку master;
git status — проверяем, точно ли на мастере.


git checkout -b 123  - создание новой ветки 123
clear - очистить

git merge 123:   смерджим  123 ветку в master

https://git-scm.com/book/ru/v2
https://git-scm.com/downloads
https://desktop.github.com/


# ФУНКЦИИ
def a_function():
    print('fasfasfsfacacsasdasdds')
    pass #- пустая операция  (заглушка для функции)

def add(a, b):
    return (a + b) # завершает работу функции и возвращает указанное значение в место вызова функции
print(add(2, 3))

def many(*args, **kwargs):
    print(args)
    print(kwargs)
many(1, 2, 3, 5, 6, 4, 3, 2, 'yuuyggjhgjhgj', name='mike', job='programmer')

    global  a # объявление а глобальной.Но нужно быть осторожным


a = lambda x, y: x * y  # упрощенный вариант функции только для 1 инструкции, с if, for,while не работает
print(a(2, 3))