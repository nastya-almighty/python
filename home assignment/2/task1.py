w = str(input('Введите ваше число = '))
res_str = w.replace('.', '')
res_str2 = res_str.replace(',', '')
res_str3 = res_str2.replace('-', '')

sum = 0
result = [int(i) for i in res_str3]


for j in result:
    sum += j

print(f"Сумма цифр в вашем числе - {sum}")