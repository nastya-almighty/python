from datetime import datetime
import math
import time

z = int(round(time.time()*1000))
current_datetime = datetime.now()
print(current_datetime)

N = int(input('Сколько чисел будет в вашем списке? '))
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

x = str(current_datetime)

res_str = x.replace('.', '')
res_str1 = res_str.replace(':', '')
res_str2 = res_str1.replace('-', '')
res_str3 = res_str2.replace(' ', '')

print(res_str3)

result = [int(i) for i in res_str3]
del result[:14]


array = []

for i in result:
    array.append(((i * math.pi) * math.e % 1) * z)

print(array)

y = str(array)
res = y.replace(',', '')
res2 = res.replace(' ', '')
res3 = res2.replace('.', '')
res4 = res3.replace('[', '')
res5 = res4.replace(']', '')



list2 = [int(i) for i in res5]
list1 = []

for i in list2:
    list1.append(i * z)


y1 = str(list1)
ress = y1.replace(',', '')
ress2 = ress.replace(' ', '')
ress3 = ress2.replace('.', '')
ress4 = ress3.replace('[', '')
ress5 = ress4.replace(']', '')

print(ress5)
print(len(ress5))


list3 = [int(i) for i in ress5]
list4 = []

for i in list3:
    list4.append(i)

print(list4)