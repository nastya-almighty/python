print ('hello world')

a = 123 #int
b = 1.23 #float

print(a)

s = 'qwerty' #str
# print(s) # вывод строки

print (a, ' - ', s)
print ('{1} - {2} - {0}'.format(a, b, s))
print (f"{a} - {b} - {s}")

f = True #boolean
print(f)

list = [1, 2, 3]
print(list)

print ('Введите x')
x = int(input())
print (x)

print(a+x)

a = 1 > 4 and 5 > 2
print(a) # False

func = 1
T = 4
y = 144

print(func<y>x)

g = 1 > 2 or 4 < 6
print(g)

arr = [1, 2, 3, 4]
print(2 in arr)

is_even = arr [1] % 2 == 0
print (is_even)



w = int(input('w = '))
v = int(input('v = '))
if w > v:
    print (w)
else:
    print(v)


original = 23573
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print ('Пожалуй, хватит')
print(inverted)


for i in 1,2,3,4:
    print (i**2)


list = range(1, 10, 2)
for i in list:
    print(i)



text = 'я обожаю кенгуру!!'
print(len(text))

colors = ['red','blue','green']
colors.append('gray') # добавить в конец
colors.remove('red') # удаляем из списка

del colors [2] # удалить элемент

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print (f(arg))