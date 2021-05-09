'''
По данному целому числу N распечатайте все квадраты натуральных чисел,
не превосходящие N, в порядке возрастания.

Формат ввода

Вводится натуральное число.

Формат вывода

Выведите ответ на задачу.
'''

n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2, end=' ')
    i += 1
