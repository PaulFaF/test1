from random import *

print('Добро пожаловать в числовую угадайку')


def is_valid(num, gran):
    if 1 <= int(num) <= gran:
        return True
    else:
        return False
while 1 != 2:
    n = int(input('Введите правую границу '))
    r = randint(1, n)
    print(r)
    count = 0
    while 1 != 2:
        x = input('Введите число ')
        count += 1
        if x.isdigit() and is_valid(x, n):
            x = int(x)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            continue
        if x < r:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif x > r:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        else:
            print('Вы угадали, поздравляем! Количество попыток -', count)
            break
    if input('Для повтора игры нажмите "Да" без кавычек ') == 'Да':
        continue
    else:
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')