# Этот вариант - если мы не хотим, чтобы при вводе пользователем нечетного числа у нас число в серединке не умножалось само на себя, 
# а оставалось в результирующем списке без изменений.

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

    if N % 2 == 0:
        for i in range(x):
            result.append(list[i] * list[len(list) - 1 - i])
    
    else:
        for i in range(x - 1):
            result.append(list[i] * list[len(list) - 1 - i])
        result.append(list[x - 1])
    return result

print(f"Произведение пар чисел вашего списка - {Mult(array)}")
