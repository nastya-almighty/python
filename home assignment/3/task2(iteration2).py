# В этом варианте, если пользователь вводит нечетное число, то число в середине списка умножается само на себя, как указано в задании.

import random

N = int(input('Сколько чисел будет в списке? '))
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))


array = []
for i in range(N):
    array.append (random.randint (min, max))

print(array)

def Mult(list):
    x = (len(list) + 1) // 2

    result = []
    for i in range(x):
        result.append(list[i] * list[len(list) - 1 - i])
    return result

print(f"Произведение пар чисел вашего списка - {Mult(array)}")