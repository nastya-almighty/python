print('Создаем последовательность чисел')
N = int(input('Сколько чисел будет в вашей последовательности? '))

list = []
for x in range(N):
    v = int(input(f"Введите число {x + 1}: "))
    if v in list:
        list.remove(v)
    else:
        list.append(v)

print(list)
