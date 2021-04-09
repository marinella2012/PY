'''
На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не
превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.
'''


def binary_search(arr, x, left, right):

    if right <= left:
        return -1
    if arr[left] >= x:
        return left + 1
    mid = (left + right) // 2
    if arr[mid-1] < x <= arr[mid]:
        return mid + 1
    elif x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


if __name__ == '__main__':
    days = int(input())
    n = [int(i) for i in input().split()]
    price = int(input())
    a = binary_search(n, price, left=0, right=days)
    b = binary_search(n, price*2, left=0, right=days)
    print(a, b)


'''
Ввод:
6
1 2 4 4 6 8
3

Вывод:
3 5
'''
