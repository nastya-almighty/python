import random

N = int(input('Сколько чисел будет в списке? '))
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

array = []
for i in range(N):
    array.append (random.randint (min, max))

print(array)

def OddSum (list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum

print(f"Сумма элементов списка на нечетных позициях: {OddSum(array)}")