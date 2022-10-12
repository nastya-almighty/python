# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

N = int(input('Сколько чисел будет в списке? '))
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))


array = []
array2 = []
for i in range(N):
    x = round(random.uniform (min, max), 2)
    array.append (x)
    array2.append (round((x % 1), 2))

print(array)

minvalue = array2[0]
maxvalue = array2[0]

for j in array2:
    if j < minvalue:
        minvalue = j
    if j > maxvalue:
        maxvalue = j

print(f'Разница между максимальным и минимальным значениями дробной части элементов: {round((maxvalue - minvalue), 2)}')
