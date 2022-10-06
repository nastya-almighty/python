n = int(input('Введите ваше число = '))
sum = 0

for i in range(1, n + 1):
    x = (1 + 1 / i) ** i
    sum += x
    print(sum)
    
print(f"Cумма чисел последовательности - {sum}")