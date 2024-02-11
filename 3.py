print('Введите текст. Для выхода напишите: Exit')
text = str(input())


def sntext(a):
    if a.islower() and a.count('_'):
        a = text.capitalize()
        a = list(a)
        for i in range(len(a)):
            if a[i] == '_':
                a[i] = ''
                a[i + 1] = a[i + 1].upper()
        a = ''.join(a)
    elif a.isalnum():
        a = list(a)
        for i in range(len(a)):
            if a[i] == a[i].upper() and i != 0:
                a[i] = '_' + a[i].lower()
            else:
                a[i] = a[i].lower()
        a = ''.join(a)
    else:
        a = "Не корректный ввод"
    return a


while text != 'Exit':
    print('Ответ:',sntext(text))
    print('Введите текст. Для выхода напишите: Exit')
    text = str(input())
else:
    print('Работа завершена')