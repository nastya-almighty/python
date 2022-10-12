numbers = ['one', 'two', 'three']
data = open('file.txt', 'a') # дописываем
data.writelines(numbers)
data.close()

# data = open('file.txt', 'w') перезапись файла
# data = open('file.txt', 'r') чтение

with open('file.txt', 'a') as data:
    data.write('line 1\n')

# exit() # заканчиваем выполнение программы

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()