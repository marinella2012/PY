'''
Даны два целых числа. Программа должна вывести число "1", если первое число
больше второго, число "2", если второе больше первого или число "0", если они
равны.

Формат ввода

Вводятся два целых числа.

Формат вывода

Выведите ответ на задачу.

Примечания

Эту задачу желательно решить с использованием каскадных инструкций
if... elif... else.
'''

a = int(input())
b = int(input())
if a >= b:
    print(a)
else:
    print(b)
