import math

def Pi():
    m = 0
    sum = 1 - (1 /9)

    for i in range (2, 30, 2):
        sum += ((1 / ((5 + m) * (3 ** i))) - (1 / ((7 + m) *(3 ** (i + 1)))))
        m += 4

    p = math.sqrt(12)*sum
    return p

pres = str(input('С какой точностью рассчитываем число Пи? '))

print(f"Пи равно {round(Pi(), len(pres) - 2)}")