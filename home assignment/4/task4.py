import random

dict_ = {
    0: "\u2070",
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
}

k = int(input('Задайте натуральную степень k, в которую мы будем возводить многочлен: '))

if k > 9:
    print('У нас не получится красиво вывести результат, если степень больше 9.')
    exit()

if k == 0:
    print(random.randint (0, 100))
    exit()

list = []

while k > 1:
    w = random.randint (0, 100)
    if w != 0:
        list.append(f"{w}'x'{dict_[k]}")
    k -= 1
y = random.randint (0, 100)
if y != 0:
    list.append(f'{y}x')
c = random.randint (0, 100)
if c != 0:
    list.append(c)


string = str(list)

for j in ["'", '"', '[']:
    if j in string:
        string = string.replace(j, '')
string = string.replace(']', ' = 0')
string = string.replace(',', ' +')
string = string.replace('1x', 'x')


print(string)