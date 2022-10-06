a = {1, 2, 3}
b = {4, 5, 6}

c = a.copy() # копируем
d = a.union(b) # объединяем множества
print(d)

i = a.intersection(b) # пересечение
dl = a.difference(b)
dr = b.difference(a)