# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых 
# и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

import random

x = int(input('Сколько чисел будет в вашей последовательности? '))
max = int(input('Каким будет максимальное значение? '))

array = [random.randint(0, max) for i in range(x)]
print()
print(f'Наш список: {array}')

locate = set()
double = {x for x in array if x in locate or locate.add(x)}

print(f'Список уникальных элементов последовательности: {locate.difference(double)}')
print(f'Список дублирующихся элементов последовательности: {double}')
print(f'Cписок без дубликатов: {locate}')

print()
print('Если мы хотим сохранить порядок:')
print()

uni = [i for i in array if i not in double]
print(f'Список уникальных элементов последовательности: {uni}')
locate2 = list(dict.fromkeys(array))
double2 = [i for i in locate2 if i not in uni]
print(f'Список дублирующихся элементов последовательности: {double2}')
print(f'Cписок без дубликатов: {locate2}')