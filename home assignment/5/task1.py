# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import codecs

path = r'C:\Users\Acer\Desktop\geekbrains\python\home assignment\5\Dancing Men.txt'
f = codecs.open(path, "r", "utf-8")
data = f.read()
f.close()

words = data.split()

def contains (string, key):
    if key in string:
        return True
    else:
        return False

li = list(filter(lambda i: contains(i, 'а') and contains(i, 'б') and contains(i, 'в'), words))
res = [i for i in words if i not in li]

newtext = str(res)

for j in ["',","'",'[', ']']:
    if j in newtext:
        newtext = newtext.replace(j, '')
        

print(newtext)
print()
print(f"Мы удалили слова с буквами абв, то есть: {li}")

