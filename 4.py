import string

s = string.ascii_lowercase
su = string.ascii_uppercase


def cesar(mtest, mkey, mch):
    a = []
    if mtest.isalpha():
        mkey = mkey - mkey // 26 * 26
        if mch == 1:
            for i in mtest:
                if s.find(i.casefold()) + mkey >= 25:
                    if i.islower():
                        a += s[s.find(i) - 25 + mkey]
                    else:
                        a += su[su.find(i) - 25 + mkey]
                else:
                    if i.islower():
                        a += s[s.find(i) + mkey]
                    else:
                        a += su[su.find(i) + mkey]
        elif mch == 0:
            for i in w:
                if s.find(i.casefold()) - mkey < 0:
                    if i.islower():
                        a += s[s.find(i) + 25 - mkey]
                    else:
                        a += su[su.find(i) + 25 - mkey]
                else:
                    if i.islower():
                        a += s[s.find(i) - mkey]
                    else:
                        a += su[su.find(i) - mkey]

        else:
            a = 'Не корректные входные данные'
        return ''.join(a)
    else:
        return 'Не корректные входные данные'


print('!E - Выход\nШифр цезаря. Введите текст:')
w = input()
print('!E - Выход\nВведите ключ:')
k = int(input())
print('!E - Выход\nВыберите действие:\n1 - Зашифровать\n0 - Расшифровать')
m = int(input())

while w or k or m != '!E':
    print('Результат:', cesar(w, k, m))
    print('!E - Выход\nШифр цезаря. Введите текст:')
    w = input()
    print('!E - Выход\nВведите ключ:')
    k = int(input())
    print('!E - Выход\nВыберите действие:\n1 - Зашифровать\n0 - Расшифровать')
    m = int(input())
else:
    print('Работа завершена')
