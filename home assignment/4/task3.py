print('Создаем последовательность чисел')
N = int(input('Сколько чисел будет в вашей последовательности? '))

list = []
for x in range(N):
    list.append(int(input(f"Введите число {x + 1}: ")))

result = set()
for item in list:
    result.add(item)

print(f"Уникальные элементы вашего списка - {result}")