import sympy
from sympy import sympify

data1 = open("text1.txt", "r")
line1 = data1.readline()
data2 = open("text2.txt", "r")
line2 = data2.readline()

line1 = line1.replace('= 0', '+')
line2 = line2.replace('= 0', '')
newline = line1 + line2

sympy_new = sympify(newline)
print(sympy_new)
















