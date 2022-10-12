n = int(input('Введите ваше число: '))

def Mults(n):
    result = []
    i = 2
    while i <= n:
        if n % i == 0:
            result.append(i)
            n /= i
        else:
            i += 1
    return result

if n > 1:
    print(f"Разложим на простые множители: {Mults(n)}")
else:
    print('Чтобы разложить натуральное число на простые множители, оно должно быть больше единицы.')