import random

N = int(input('Введите ваше число = '))

if N < 93:
    print('Чтобы мы могли перемножить числа с данными в условии индексами, в следующий раз задайте число не менее 93')

else:
    print(f'Создаем список из {N} чисел в промежутке от {-N} до {N}')
    mult = 1

    array = []
    for i in range(N):
        array.append (random.randint (-N, N))

    print(array)

    list = [45, 20, 4, 92, 10, 5, 79, 39, 63, 67, 2, 52, 83, 59, 18, 41, 11, 22, 90, 3]

    for j in range(len(list)):
        mult *= array[list[j]]

    print(f"Произведение элементов с индексами 45, 20, 4 ... итд - {mult}")

