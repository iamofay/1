print('Введите число. Для выхода напишите: Exit')
number = input()


def crash(a):
    if a.isnumeric():
        a = list(a)
        for i in range(len(a) % 3 - 1, len(a) - 1, 3):
            a[i] += ' '
        a = ''.join(a)
    else:
        a = 'Неверный формат данных'
    return a


while number != 'Exit':
    print('Ответ:', crash(number))
    print('Введите число. Для выхода напишите: Exit')
    number = input()
else:
    print('Работа завершена')
