# Реализуйте алгоритм перемешивания списка

N = int(input('Сколько чисел будет в вашем списке? '))
min = int(input('Введите минимальное значение в будущем списке: '))
max = int(input('Введите максимальное значение в будущем списке: '))

import random

array = []
for i in range(N):
    array.append (random.randint (min, max))

print(array)

shuffle = []

for j in range(len(array)):
    x = random.randint(0, N - 1)
    shuffle.append(array[x])
    del array[x]
    N -= 1

print(shuffle)