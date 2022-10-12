# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


e = int(input('Введите ваше число: '))
if e < 0:
    print('Наша программа пока к такому не готова :)')
    exit()

def Binary(x):
    if x == 0:
        return 0

    else:

        array = []

        while x > 0:
            if x % 2 == 0:
                array.insert(0, 0)
            else:
                array.insert(0, 1)
    
            x //= 2

        string = str(array)
        for j in [' ', ',', '[', ']']:
            if j in string:
                string = string.replace(j, '')
        return string

    
print(f"В двоичной системе счисления ваше число равно {Binary(e)}")
