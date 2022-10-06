# import 'название файла'

# import hello as h

# print(h.f(1))

from ast import iter_child_nodes


def new_string (symbol, count):
    return symbol * count

print(new_string('!', 5))

def new_string1 (symbol, count = 3):
    return symbol * count

print(new_string1('!'))


def Fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

list = []
for e in range(1, 10):
    list.append(Fibo(e))

print(list)

def conc (*params):
    # res: str = ""
    # res: int = 0
    res = 0
    for item in params:
        res += item
    return res

print(conc('a', 'b', 'c', 'w'))