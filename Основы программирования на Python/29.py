'''Шахматный король ходит по горизонтали, вертикали и диагонали, но только на
1 клетку. Даны две различные клетки шахматной доски, определите, может ли
король попасть с первой клетки на вторую одним ходом.

Формат ввода:
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер
столбца и номер строки сначала для первой клетки, потом для второй клетки.

Формат вывода:
Программа должна вывести YES, если из первой клетки ходом короля можно попасть
во вторую или NO в противном случае.

'''

a = int(input())
b = int(input())
if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)
