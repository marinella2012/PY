'''
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи
есть копилка, в которую каждый день он может добавлять деньги (если, конечно,
у него есть такая финансовая возможность). В процессе накопления Вася не
вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке
было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить

первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода.
В первой строке дано число дней n, по которым велись наблюдения за Васиными
накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке
неубывания. Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда.
Это число не превосходит 106.

Формат вывод.
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера
дня.
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
