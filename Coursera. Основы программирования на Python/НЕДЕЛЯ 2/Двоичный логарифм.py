'''
По данному натуральному числу N выведите такое наименьшее целое число k,
что 2ᵏ≥N.

Операцией возведения в степень пользоваться нельзя!

Формат ввода:
Вводится натуральное число.

Формат вывода:
Выведите ответ на задачу.
'''
n = int(input())
k = 1
i = 0
while k < n:
    k *= 2
    i += 1
print(i)
