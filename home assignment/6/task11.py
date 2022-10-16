# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный
# добавьте скобки

x = str(input('Введите ваше арифметическое выражение - '))

def String(string):
    g = ''
    for j in string:
        if j.isdigit():
            g += j
        else:
            g += f' {j} '
    a = g.split()
    return a6

a = String(x)
print(a)
s1 = ''

for i in a:
    if i == '(':
        s1 += i
        if i == ')':
            break

s2 = String(s1)




