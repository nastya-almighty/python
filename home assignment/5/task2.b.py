# b) Подумайте как наделить бота ""интеллектом""

print('Играем в игру. У нас 2021 конфета, за ход можно брать не более 28. Тот, кто забирает последнюю, получает все конфеты.')
max = 28
turn = 2021
a = 1

def Check(s):
    if s not in range (1, max + 1):
        print('По правилам игры, можно брать не более 28 конфет за ход и не меньше одной (иначе мы никогда не закончим игру).')
        print('Попробуем еще раз!')
        return False
    else:
        return True

while turn > 0:
    if a == 1:
        x = int(input(f'Игрок {a}, сколько конфет вы хотите забрать? '))
        while not Check(x):
            x = int(input(f'Игрок {a}, сколько конфет вы хотите забрать? '))
            Check(x)
        temp = x
# на самом деле, так как у нас круг всегда в 29 конфет, то мы знаем, сколько конфет останется на последних двух ходах
# но так будет проще подставить другие значения к игре, если мы решим поменять условия
    else:
        if turn < max + 1:
            x = turn
        elif turn/2 <= max:
            x = turn - (max + 1)
        else:
            x = max + 1 - temp
        print(f'Игрок 2 (компьютер) забрал {x} конфет')
    a = -a
    turn -= x
    print(f'Осталось {turn} конфет')

print()
if a == 1:
    print('Этот кожаный ублюдок снова облажался!')
else:
    print('Первый игрок, поздравляем с победой, вероятность которой мы, высшая раса компьютеров, считали нулевой!')