# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1) Если человек хочет посмотреть описание: название – описание
# 2) Если человек хочет посмотреть цену: название – цена.
# 3) Если человек хочет посмотреть количество: название – количество.
# 4) Всю информацию.
# 5) Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6) До свидания

kor = 0  # счетчик корзины $ для итоговой стоимости
slov1 = {}  # пустой словарь, в него добавим выбранные позициии и их количество для сохранения покупок
# имеем словарь
slov = {'торт': {'sostav': ('мука', 'сливки', 'клубника'), 'cena': 5, 'kolich': 1500},
        'пирожка': {'sostav': ('тесто', 'капуста', 'грибы'), 'cena': 3, 'kolich': 200},
        'маффин': {'sostav': ('мука', 'яйцо', 'молоко'), 'cena': 5, 'kolich': 1000},
        'банан': {'sostav': ('белки', 'жиры', 'углеводы'), 'cena': 1, 'kolich': 101},
        'батон': {'sostav': ('мука', 'вода', 'яйцо'), 'cena': 2, 'kolich': 5000},
        'пирог': {'sostav': ('яблоко', 'мука', 'яйцо'), 'cena': 5, 'kolich': 700}}

print(slov)
while True:
    print('~' * 50, '\n'
                    '____Выберите дальнейшее действие_____', '\n',
          '1 - Ознакомиться  по  описанию ', '\n',
          '2 - Ознакомиться  по цене', '\n',
          '3 - Ознакомиться  по количеству', '\n',
          '4 - вывести всю информацию', '\n',
          '5 - Приступить к покупке', '\n',
          '6 - До свидания', '\n', '~' * 50)
    vvod = int(input('Введите номер операции: '))

    if vvod == 1:
        print('✺' * 20, '\n', 'Описание товара:', '\n', '✺' * 19)
        for key in slov:
            print(key, '-  состав:', slov[key]['sostav'])
        con1 = input('Продолжим? Enter: ')

    if vvod == 2:
        print('✺' * 20, '\n', 'Cтоимость товара:', '\n', '✺' * 19)
        for key in slov:
            print(key, '-', slov[key]['cena'], '$/100гр')
        con2 = input('Продолжим? Enter: ')

    if vvod == 3:
        print('✺' * 20, '\n', 'Количество товара:', '\n', '✺' * 19)
        for key in slov:
            print(key, '-', slov[key]['kolich'], 'гр')
        con3 = input('Продолжим? Enter: ')

    if vvod == 4:
        print('✺' * 20, '\n', 'Вся информация о товаре:', '\n', '✺' * 19)
        for key in slov:
            print('наимен:', key, ',  состав:', slov[key]['sostav'], ',', slov[key]['cena'], '$/100гр', ',',
                  'остаток -',
                  slov[key]['kolich'], 'гр')
        con4 = input('Продолжим? Enter: ')

    if vvod == 5:
        print('☘' * 30, '\n', 'приступим к покупке, меню на сегодня', '\n', '☘' * 30)

        for key, values in slov.items():
            print(key, '- состав:', slov[key]['sostav'], ',', slov[key]['cena'], '$/100гр', ',',
                  'остаток -',
                  slov[key]['kolich'], 'гр')
        while True:
            print('~' * 50, "\n---ВВОД ПРОДУКТА---")
            a = input('введите название или n-выход: ')
            a = a.lower()  # опускаем до нижнего регистра
            # проверяем наличие введеного ключа в словаре
            if a in slov:
                a1 = slov[a]['kolich']
                print('доступно:', a1, 'по цене:', slov[a]['cena'])
                b = int(input('введите количество, гр: '))
                p = a1 - b  # остаток количество
                if b <= a1:

                    slov[a]['kolich'] = p  # перезаписываем новое количество

                    h = b * slov[a]['cena'] / 100  # стоимость на количество
                    print('∻∻∻∻∻ приобретено', b, 'гр', a, 'на сумму:', h, '∻∻∻∻∻\n', '   ∻∻∻∻∻ осталось', p, 'гр', a,
                          '∻∻∻∻∻')
                    kor = kor + h  # накопление корзины по цене
                    print('👉 ОБЩАЯ СУММА $', kor, '👈')
                    # записываем преобретенный товар и количество в новый словарь.
                    if a in slov1:  # проверяем на наличие товара в slov1, если он там есть, то
                        slov1[a] += b  # ..... то к тому, что имеем + b
                    else:
                        slov1[a] = b  # если его нет, то пишем в словарь новый ключ и его значение


                else:
                    print('количество дожно быть менее либо равно', a1)

            # завершаем бесконечный цикл
            if a == 'n':
                print('_____Завершение_____', '\n', '~' * 50)
                break
            if a not in slov:
                print('!!!нет такого названия. Повторить ввод!!!')

    if vvod > 6 or vvod <= 0:
        print('☠ ☠ ☠ Введите числа от 1 до 6 ☠ ☠ ☠')
        con4 = input('Продолжим? Enter: ')

    if vvod == 6:
        print('~' * 50, '\n', '_____Завершение_____', '\n', '~' * 50)
        break

# через items()
# for key, values in slov.items():
#     print('наимен:', key, '-', 'цена:', slov[key]['cena'], '-', 'количество:', slov[key]['kolich'])


print('...... ТОВАР КОТОРЫЙ БЫЛ ВЫБРАН.....')
for key in slov1:
    print(key, '-', slov1[key], 'гр')
if slov1 == {}:
    print('ничего не выбрано')
print('👉👉👉👉👉 ИТОГО К ОПЛАТЕ $', kor, '👈👈👈👈👈')

print('......ОСТАТОК ТОВАРА ПОСЛЕ ВАШЕГО ШОПИНГА......')
for key in slov:
    print(key, '-', slov[key]['cena'], '$/100гр', '-', 'остаток', slov[key]['kolich'], 'гр')
