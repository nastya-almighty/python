x = str(input('Введите ваше число: '))

def Decimal (q):
    res = [int(i) for i in x]

    num_dec = 0
    for j in range(len(res)):
        num_dec = num_dec + res[j] * (2**(len(res) - j - 1))
    print (num_dec)
    return num_dec

Decimal(x)