# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import codecs

path = r'C:\Users\Acer\Desktop\geekbrains\python\home assignment\5\origin4.txt'
f = codecs.open(path, "r", "utf-8")
data = f.read() + ' '
f.close()

res = ''
count = 1

for i in range(len(data) - 1):
    if data [i + 1] != data [i]:
        res += f'{count}{data[i]}'
        count = 1
    else:
        count += 1

print(f'Зашифруем ваш текст: {res}')

decoding = ''
count = ''
for j in res:
    if j.isdigit():
        count = j
    else:
        decoding += j * int(count)

print()
print(f'А теперь расшифруем: {decoding}')

g = open('res.txt', 'w')
g.write(res)
g.close