# Задача 1.1:
# В деревне живет 12 лесорубов . Для вырубки леса они были разделены рандомно на 3 равные команды. Вывести список(множество) всех участников
# кто попал в команды и список(множество) кто не попал, и так же список(множество) кто попал одновременно в 2 или 3 команды.
import random
a0 = set(range(1, 13))
# создаем рандомную команду из цифр. цифры не должны повторяться поэтому используем множество,
# но и количество должно быть обязательно 4 - поэтому создаем цикл с проверкой длины множества
# команда 1
v1 = 0
while v1 < 4:
    a1 = set([random.randint(1, 12) for i in range(4)])
    v1 = len(a1)
print(' команда 1:', a1)
# команда 2
v2 = 0
while v2 < 4:
    a2 = set([random.randint(1, 12) for i in range(4)])
    v2 = len(a2)
print(' команда 2:', a2, )
# команда 3
v3 = 0
while v3 < 4:
    a3 = set([random.randint(1, 12) for i in range(4)])
    v3 = len(a3)
print(' команда 3:', a3, )
print('попали в команды:', a1 | a2 | a3)
print('Не попали в команды:', a0 - (a1 | a2 | a3))
print('В две команды одновременно попали:', a1 & a2,',', a1 & a3,',', a2 & a3)
print('в три команды одновременно попали:', a1 & a2 & a3)



# Задача 1.2:
# В команде 38 программиста  21 спецы в Python, 18 - java, 16 спецы и python и java . Сколько ложных программистов в команде
# которые не знают java и python ?

prg = 38
Python = set(range(1, 22))
print(Python)
java = set(range(22, 40))
print(java)
Pythonjava = set(range(1, 17))
a = Python | java
print(a)
b = len(a - Pythonjava)  # всего кто знает языки
print(b)
print('колличество программистов которые не знают java и python', prg - b)



# Задача 1.3:
# Имеем 12 программистов. Необходимо выполнить 3 проекта за 1 рабочий день. рабочий день - 8ч.  Были организованы 2 равные
# команды по 6 чел и спланированы трудочасы каждого программиста (рандомно).
# Вывести списки кто не попал в команду и кто попал в команды. Списки кто больше всего времени потратил
# на выполнение проектов и кто меньше всего времени затратил.

import random

# формируем  12 программистов через множество
a0 = set(range(1, 13))
print(' программисты:', a0)
# создаем рандомную команду из цифр. цифры не должны повторяться поэтому используем множество,
# но и количество должно быть обязательно 6 - поэтому создаем цикл с проверкой длины множества
# команда 1
v1 = 0
while v1 < 6:
    a1 = set([random.randint(1, 12) for i in range(6)])
    v1 = len(a1)
print(' команда 1:', a1, '----проверка, количество чел в команде:', v1)
# команда 2
v2 = 0
while v2 < 6:
    a2 = set([random.randint(1, 12) for i in range(6)])
    v2 = len(a2)
print(' команда 2:', a2, '----проверка, количество чел в команде:', v2)

# рандомно выставляем трудочасы каждому члену команды, применяем словарь
d1 = {i: random.randint(1, 8) for i in a1}
d2 = {i: random.randint(1, 8) for i in a2}
# d3 = {i: random.randint(1, 8) for i in a3}

print('трудочасы команды 1 на выполнение проекта 1:', d1)
print('трудочасы команды 2 на выполнение проекта 2:', d2)
# print('трудочасы команды 3 на выполнение проекта 3:', d3)

c = a1 | a2
print('в команды попали следующие программисты:', c)
c1 = a0 - c
print('в команды Не попали следующие программисты:', c1)
c2 = a1 & a2
print('одновременно в двух командах следующие программисты:', c2)

print('общие трудочасы на реализацию проекта 1:', sum(d1.values()), ', max трудоемкость', max(d1.values()),
      ',  min трудоемкость', min(d1.values()))
print('общие трудочасы на реализацию проекта 2:', sum(d2.values()), ', max трудоемкость', max(d2.values()),
      ',  min трудоемкость', min(d2.values()))