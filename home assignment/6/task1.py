# 1 – Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Тупой вариант решения задачи:

import sympy
from sympy import sympify

string = str(input('Введите ваше арифметическое выражение - '))
print(sympify(string))