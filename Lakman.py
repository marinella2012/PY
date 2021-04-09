import time
import copy
import random


def angle(h, m):
    # Вычисление угла между стрелками часов
    res = abs(30 * h - 5.5 * m)
    while res > 180:
        res -= 360
    return abs(res)


def min_finder(array):
    # Бинарный рекурсивный поиск минимального числа в отсортированном списке
    # с цикличным сдвигом
    a = len(array)
    if a == 2:
        return array[0] if array[0] < array[1] else array[1]
    if array[a // 2] >= array[-1]:
        return min_finder(array[a // 2:])
    else:
        return min_finder(array[:(a // 2) + 1])


def min_finder2(array):
    # Поиск минимального элемента в отсортированном списке итерацией
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return array[i]
    return array[0]


def compare(letter, magazine):
    # Проверка вхождения подстроки letter в строку magazine
    d1 = {}
    d2 = {}
    for i in letter:
        d1[i] = 0
    for i in letter:
        d1[i] += 1
    for i in magazine:
        d2[i] = 0
    for i in magazine:
        d2[i] += 1

    for k in d1.keys():
        try:
            d2[k] -= 1
        except KeyError:
            return False
        if d2[k] < 0:
            return False
    return True


def only_char(string):
    # Проверка уникальности символов в строке, времы выполнения O(n**2)
    for i in string:
        if string.count(i) > 1:
            return False
    return True


def only_char_recur(string):
    # Рекурсивная проверка уникальности символов в строке,
    # время выполнения О(n**2)
    if len(string) == 1:
        return True
    if string.count(string[0]) > 1:
        return False
    else:
        return only_char_recur(string[1:])


def timer(func, *args, iterations=1000, need_result=False, **kwargs):
    # Таймер, измеряющий время выполнения функции.
    # func - Функция, которую проверяем
    # *args - все неименные аргументы для функции
    # iterations - коилчество запусков функции, по умолчанию 1000
    # need_result - выводить ли результат работы функции
    # **kwargs - именованные аргументы
    start_time = time.perf_counter()
    answer = None
    i = 0
    try:
        print('Beginning...')
        for i in range(iterations):
            answer = func(*args, **kwargs)
    except Exception as e:
        print('Error occurred: \'%s\'' % e)
    else:
        print('No errors occurred during working')
    finally:
        spent = time.perf_counter() - start_time
        if need_result:
            result = 'Function \'%s\' returned \'%s\'\nAmount of iterations: %s\nTime spent: %s\n' % (
                func.__name__, answer, i+1, spent
            )
        else:
            result = 'Function \'%s\'\nAmount of iterations: %s\nTime spent: %s\n' % (
                func.__name__, i+1, spent
            )
    print(result)
    return answer


def cycle_move(string, n):
    # Цикличный сдвиг строки на n символов вправо, время выполнения O(n)
    for i in range(n):
        string = string[-1] + string[:-1]
    return string


def cycle_move2(string: str, n: int):
    # Цикличный сдвиг строки на n символов вправо, время работы O(1)
    return string[-n:] + string[:-n]


def is_substring(sub: str, string: str):
    # Проверка вхождения подстроки sub в строку string, время работы O(n**2)
    is_substring.calls += 1
    return True if sub in string else False

# Количество вызовов функции выше


is_substring.calls = 0


class MyNode:
    # Узел для односвязного списка
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return repr(self.data)


class MyLL:
    # Односвязный ссписок
    def __init__(self, *args):
        self.length = 0
        if len(args) == 0:
            self.first = None
        else:
            # Возможность создания списка сразу при создании экземпляра
            # instance = MyLL(*args)
            self.length = 1
            self.first = MyNode(args[0])
            for i in args[1:]:
                self.append(i)

    def __repr__(self):
        # Вывод на экран содержимого связанного списка
        res = []
        curr = self.first
        while curr:
            res.append(repr(curr))
            curr = curr.next_node
        return 'LinkedList [' + ', '.join(res) + ']'

    def __getitem__(self, index):
        # Метод для получения элемента списка по индексу
        if not self.first:
            return None
        curr = self.first
        i = 0
        while i < index:
            if curr.next_node:
                i += 1
                curr = curr.next_node
            else:
                raise StopIteration
        return curr.data

    def __iadd__(self, other):
        self.append(other)
        return self

    def __radd__(self, other):
        tmp = copy.deepcopy(self)
        tmp.prepend(other)
        return tmp

    def __add__(self, other):
        tmp = copy.deepcopy(self)
        tmp.append(other)
        return tmp

    def __len__(self):
        return self.length

    def append(self, value):
        self.length += 1
        if not self.first:
            self.first = MyNode(data=value)
            return
        curr = self.first
        while curr.next_node:
            curr = curr.next_node
        curr.next_node = MyNode(data=value)

    def prepend(self, value):
        self.length += 1
        self.first = MyNode(data=value, next_node=self.first)

    def clear(self):
        self.__init__()

    def find(self, key):
        # Линейный поиск значений
        curr = self.first
        while curr and curr.data != key:
            curr = curr.next_node
        return curr

    def remove(self, key):
        # Удаление элементов
        curr = self.first
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next_node
        if prev is None:
            self.first = curr.next_node
            self.length -= 1
        elif curr:
            prev.next_node = curr.next_node
            curr.next_node = None
            self.length -= 1

    def reverse(self):
        # "Разворот" списка
        curr = self.first
        prev_node = None
        while curr:
            next_nd = curr.next_node
            curr.next_node = prev_node
            prev_node = curr
            curr = next_nd
        self.first = prev_node

    def end_finder(self, index):
        # Нахождение i-го элемента с конца списка
        self.reverse()
        curr = self.first
        while index:
            try:
                curr = curr.next_node
                index -= 1
            except AttributeError:
                return None
            except TypeError:
                return 'Wrong index'
        a = curr.data
        self.reverse()
        return a

    def numbers_reverse(self):
        # Вывод целого числа, сострящим из всех значений списка
        # в обратном порядке
        # Пример: список LinkedList [1,2,3] вернет 321
        res = 0
        curr = self.first
        i = 1
        while curr.next_node is not None:
            res += i * curr.data
            i *= 10
            curr = curr.next_node
        if res and curr.data:
            res += i * curr.data
        return res

    def numbers(self):
        # То же, что и метод выше, только в прямом порядке
        res = 0
        curr = self.first
        while curr.next_node:
            res = res * 10 + curr.data
            curr = curr.next_node
        res = res * 10 + curr.data
        return res

    def is_palindrome(self):
        # проверка, является ли список палиндромом
        first_iterator = second_iterator = ''
        curr = self.first
        while curr.next_node:
            first_iterator += str(curr.data)
            second_iterator = str(curr.data) + second_iterator
            curr = curr.next_node
        first_iterator += str(curr.data)
        second_iterator = str(curr.data) + second_iterator
        return True if first_iterator == second_iterator else False

    @staticmethod
    def data_swap(node1, node2):
        # Метод, меняющим информацию в 2 узлах местами
        node1.data, node2.data = node2.data, node1.data

    def sort(self, ascending=True):
        # Сортировка выбором
        if self.length < 2:
            return self
        curr = self.first
        while curr.next_node:
            iterator = curr
            while iterator.next_node:
                iterator = iterator.next_node
                if iterator.data <= curr.data:
                    if ascending:
                        self.data_swap(iterator, curr)
                else:
                    if not ascending:
                        self.data_swap(iterator, curr)
            curr = curr.next_node
        return self

    def insert(self, key, value):
        # Вставление значения в любое место списка
        if self.first is None:
            self.first = MyNode(value)
        else:
            curr = self.find(key)
            curr.next_node = MyNode(value, curr.next_node)

    def doubles_delete(self):
        # Удаление дубликатов из неотсортированного списка
        # Время выполнения O(n**2)
        if self.length > 1:
            curr = self.first
            while curr.next_node:
                iterator = curr
                while iterator.next_node:
                    prev = iterator
                    if iterator.next_node:
                        iterator = iterator.next_node
                    if iterator.data == curr.data:
                        prev.next_node = iterator.next_node
                        iterator = prev
                        self.length -= 1
                if curr.next_node:
                    curr = curr.next_node

    def doubles_delete_sorted(self):
        # Удаление дубликатов из сортированного списка, время выполнения O(k),
        # где k - размер списка
        if self.length > 1:
            curr = self.first
            while curr.next_node:
                if curr.data == curr.next_node.data:
                    curr.next_node = curr.next_node.next_node
                    self.length -= 1
                else:
                    curr = curr.next_node

    def sorted_insert(self, value):
        # Вставка значений в отсортированный список
        if self.length == 1:
            if value <= self.first.data:
                self.prepend(value)
            else:
                self.append(value)
        elif self.length == 0:
            self.first = MyNode(value)
        else:
            curr = self.first
            while curr.next_node:
                if (curr.data <= value) and (curr.next_node.data >= value):
                    curr.next_node = MyNode(value, curr.next_node)
                    break
                curr = curr.next_node
            else:
                curr.next_node = MyNode(value)


class CLinkedList:
    # Зацикленный односвязный список
    def __init__(self, cycle_start=0):
        self.first = None
        self.length = 0
        self.cycle_start = cycle_start

    def __repr__(self):
        res = []
        if self.length:
            i = 0
            curr = self.first
            while i < self.length:
                res.append(repr(curr.data))
                curr = curr.next_node
                i += 1
        return 'Cycled LinkedList [' + ', '.join(res) + ']'

    def append(self, other):
        if self.first is None:
            self.first = MyNode(other)
            self.length += 1
        else:
            curr = self.first
            counter = 1
            while counter < self.length:
                counter += 1
                curr = curr.next_node
            if self.length <= self.cycle_start:
                curr.next_node = MyNode(other)
            else:
                curr.next_node = MyNode(other, self[self.cycle_start])
            self.length += 1

    def __getitem__(self, index):
        if index >= self.length:
            raise StopIteration
        if self.length:
            curr = self.first
        else:
            return
        while index > 0:
            curr = curr.next_node
            index -= 1
        return curr.data

    def __len__(self):
        return self.length

    def cycle_finder(self):
        # Метод находит элемент списка, с которого начинается зацикливание
        if self.first is None:
            return None
        else:
            curr = self.first
            counter = 1
            while counter < self.length:
                curr = curr.next_node
                counter += 1
            return curr.next_node


class DualNode:
    # Узел для двухсвязного списка
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return repr(self.data)


class DLinkedList:
    # Двухсвязный список
    def __init__(self):
        self.first = None

    def __repr__(self):
        res = []
        if self.first is not None:
            curr = self.first
            while curr.next_node:
                res.append(repr(curr.data))
                curr = curr.next_node
            res.append(repr(curr.data))
        return 'Dual LinkedList [' + ', '.join(res) + ']'

    def append(self, other):
        if self.first is None:
            self.first = DualNode(other)
        else:
            curr = self.first
            while curr.next_node:
                curr = curr.next_node
            curr.next_node = DualNode(other, curr)


class FastLL:
    # Односвязный список с быстрой записью
    # Время записи в списки выше рано O(k), где k - размер списка
    # Время записи в FastLL - O(1)
    def __init__(self):
        self.first = None
        self.curr = None
        self.summ = 0

    def __repr__(self):
        res = []
        if self.first:
            current = self.first
            while current.next_node:
                res.append(repr(current.data))
                current = current.next_node
            res.append(repr(current.data))
        return 'FastLL [' + ', '.join(res) + ']'

    def append(self, other):
        self.summ += other
        if self.first is None:
            self.first = MyNode(other)
            self.curr = self.first
        else:
            self.curr.next_node = MyNode(other)
            self.curr = self.curr.next_node


class StackNode:
    # Узел для стэка
    def __init__(self, data, prev_node=None):
        self.data = data
        self.prev_node = prev_node

    def __repr__(self):
        return repr(self.data)


class Stack:
    # Стэк, размер по умолчанию - 60 элементов
    def __init__(self, size=60):
        self.top = None
        self.length = 0
        self.size = size

    def __repr__(self):
        res = []
        if self.top:
            curr = self.top
            while curr.prev_node:
                res.append(repr(curr.data))
                curr = curr.prev_node
            res.append(repr(curr.data))
        return 'Stack [' + ', '.join(res) + ']'

    def append(self, other):
        if self.length == self.size:
            raise MemoryError('stack overflow')
        self.length += 1
        if self.top:
            self.top = StackNode(other, self.top)
        else:
            self.top = StackNode(other)


class BTreeNode:
    # Узел для бинарного дерева
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return ('[' + repr(self.left) + ' ' + repr(self.data) + ' '
                + repr(self.right) + ']').replace('None', '')


class BTree:
    # Бинарное дерево
    def __init__(self):
        self.root = None
        self.current = None

    def __repr__(self):
        return 'BinTree: ' + repr(self.root) if self.root else 'BinTree: '

    def height(self, node):
        # Метод вычисляет размер заданной ветви
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def none_finder(self, start):
        # Метод находит ближайшую ветвь, в которой есть место для записи
        if None in (start.left, start.right):
            return start
        else:
            if self.height(start.left) > self.height(start.right):
                return self.none_finder(start.right)
            else:
                return self.none_finder(start.left)

    def append(self, value):
        if self.root is None:
            self.current = self.root = BTreeNode(value)
            return
        if None in (self.current.left, self.current.right):
            curr = self.current
        else:
            curr = self.none_finder(self.root)
            self.current = curr
        if curr.left is None:
            curr.left = BTreeNode(value)
        else:
            curr.right = BTreeNode(value)

    def clear(self):
        # Очистка дерева
        self.__init__()


def is_palindrome(s: str):
    # Рекурсивно проверяет, является ли заданная строка палиндромом
    if len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    elif s[0] == ' ':
        return is_palindrome(s[1:])
    elif s[-1] == ' ':
        return is_palindrome(s[:-1])
    else:
        return False


def zipper(string):
    # преобразует строку вида "АААА" в "А4"
    c = res = string[0]
    i = 1
    counter = 1
    while i < len(string):
        if string[i] == c:
            counter += 1
            i += 1
        else:
            c = string[i]
            i += 1
            if counter > 1:
                res += str(counter)
                counter = 1
            res += c
    if counter > 1:
        res += str(counter)
    return res


def unzipper(string):
    # Преобразует результат работы функции выше в исходную строку
    c = string[0]
    res = mul = ''
    i = 1
    while i < len(string):
        if string[i].isdigit():
            mul += string[i]
            i += 1
        elif mul:
            res += c * int(mul)
            c = string[i]
            i += 1
            mul = ''
        else:
            res += c
            c = string[i]
            i += 1
    if mul:
        res += c * int(mul)
    else:
        res += c
    return res


def prime_factors_recur(n, i=2, factors=None):
    # Рекурсивный поиск простых множителей числа
    if factors is None:
        factors = []
    if n <= i:
        factors.append(n)
        return factors
    elif n % i and i == 2:
        return prime_factors_recur(n, i + 1, factors=factors)
    elif n % i and i > 2:
        return prime_factors_recur(n, i + 2, factors=factors)
    else:
        factors.append(i)
        return prime_factors_recur(n // i, i, factors=factors)


def count_intersections(array1, array2):
    # Возвращает список, каждый i-й элемент которого является количеством
    # совпадений заданных двух списков до значения i
    # Пример:   array1 = [1, 2, 3, 4, 5]
    #           array2 = [3, 2, 1, 5, 4]
    #              res = [0, 1, 3, 3, 5]
    res = []
    for i in range(1, len(array1) + 1):
        temp1 = set(array1[:i])
        temp2 = set(array2[:i])
        res.append(len(temp1 & temp2))
    return res


def primes_to(n):
    # Возвращает список простых чисел до заданного включительно
    # Вычисляет методом решета Эратосфена
    result = list(range(2, n + 1))
    result[1] = 0
    for i in result:
        if i > 1:
            for j in range(i * 2, len(result), i):
                result[j] = 0
    return [i for i in result if i]


def prime_factors_cycle(n):
    # Разложение числа на простые множители, теперь не рекурсией, а циклом
    i = 2
    res = []
    while i <= n:
        if not n % i:
            res.append(i)
            n = n // i
        elif i == 2:
            i += 1
        else:
            i += 2
    return res


def multiply(a, b):
    res = 0
    i = 0
    while i < b:
        res += a
        i += 1
    return res


def decrease(a, b):
    i = 0
    while b < a:
        b += 1
        i += 1
    return i


def divide(a, b):
    res = b
    i = 1
    while res < a:
        res += b
        i += 1
    return i


def multi_recur(a, b, i=1, res=None):
    if not res:
        res = a
    if i >= b:
        return res
    return multi_recur(a, b, i + 1, res=res + a)


def decrease_recur(a, b, i=0):
    if b == a:
        return i
    return decrease_recur(a, b + 1, i + 1)


def divide_recur(a, b, i=1, res=None):
    if not res:
        res = b
    if res >= a:
        return i
    else:
        return divide_recur(a, b, i + 1, res + b)


def palindrome_check(text):
    # Проверка строки на палиндром, рекурсия
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return palindrome_check(text[1:-1])
    if text[0] == ' ':
        return palindrome_check(text[1:])
    if text[-1] == ' ':
        return palindrome_check(text[:-1])
    return False


def brackets(n, first=0, last=0, array=None):
    # Вывод всех правильных комбинаций из n пар скобок
    if array is None:
        n *= 2
        array = [None for i in range(n)]
    if first <= n - last - 2:
        array[last] = '('
        brackets(n, first + 1, last + 1, array)
    if first > 0:
        array[last] = ')'
        brackets(n, first - 1, last + 1, array)
    if last == n:
        if first == 0:
            return print(''.join(array))


# brackets(3, 0, 0, None)


def permutations(text):
    # Возвращает все перестановки строки
    if len(text) == 1:
        return [text]
    if len(text) == 2:
        return [text, text[::-1]]
    res = []
    for i in permutations(text[:-1]):
        for j in range(len(i), -1, -1):
            res.append(i[:j] + text[-1] + i[j:])
    return res


def amount_of_permutations(length: int):
    # Считает количество перестановок для заданной длины строки
    if length == 1:
        return 1
    else:
        return length * amount_of_permutations(length-1)


def bubble_sort(array):
    swaps = True
    result = array.copy()
    while swaps:
        swaps = False
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swaps = True
    return result


def selection_sort(array):
    res = array.copy()
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]
    return res


def merge_sort(array):
    n = len(array)
    if n < 2:
        return array

    left = merge_sort(array[:n // 2])
    right = merge_sort(array[n // 2:])

    i = j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res


def bracket_combinations(amount):
    # Вывод всех правильных скобочных последовательностей из n пар скобок
    if amount == 1:
        return {'()'}
    res = set()
    for i in list(bracket_combinations(amount - 1)):
        for j in range(len(i)):
            res.add(i[:j] + '()' + i[j:])
    return res


def quick_sort(array):
    # Быстрая сортировка
    if len(array) < 2:
        return array

    q = random.choice(array)
    left = [i for i in array if i < q]
    mid = [i for i in array if i == q]
    right = [i for i in array if i > q]

    return quick_sort(left) + mid + quick_sort(right)


def radix_sort(array, cycles=0, end=1):
    # Поразрядная сортировка
    result = []
    for i in range(10):
        for j in array:
            if j // (10 ** cycles) % 10 == i:
                result.append(j)
                if i > 0:
                    end = 0
    if end:
        return result
    else:
        return radix_sort(result, cycles + 1)


def b_search(array, x, n, i=0):
    # Бинарный поиск индекса заданного элемента в сортированном
    # списке со сдвигом
    if n < 2:
        return i

    n //= 2
    if array[0] < array[n]:
        if x < array[0]:
            return b_search(array[n:], x, n, i + n)
        elif x < array[n]:
            return b_search(array[:n], x, n, i)
        elif x == array[0]:
            return i
        else:
            return i + n
    else:
        if x < array[n]:
            return b_search(array[:n], x, n, i)
        elif x < array[0]:
            return b_search(array[n:], x, n, i + n)
        elif x == array[n]:
            return i + n
        else:
            return i


'19 21 100 101 1 4 5 7 12'
y = int(input())
x = int(input())
array = [int(i) for i in input().split()]
print(b_search(array, x, y, i=0))


def string_to_set(text: str):
    # Преобразование строки в множество, состоящее из отдельных слов
    for i in text:
        if not i.isalpha():
            text = text.replace(i, ' ')
    return set(text.lower().split())


def doc_finder(docs, words):
    # Создает список документов из docs, содержащих все слова words
    words_in_docs = {i: set() for i in words}
    for doc in docs:
        tmp_file = open(doc, 'r')
        tmp_string = tmp_file.readline()
        while tmp_string:
            for word in words:
                if word in string_to_set(tmp_string):
                    words_in_docs[word].add(doc)
                    continue
            tmp_string = tmp_file.readline()
        tmp_file.close()
    ks = list(words_in_docs.keys())
    res = words_in_docs[ks[0]]
    for i in ks[1:]:
        res = res & words_in_docs[i]
    return res


def repeats(array):
    # Выводит все дублирующиеся элементы отсортированного списка
    tmp = array[0]
    found = 0
    for i in range(1, len(array)):
        if array[i] == tmp:
            if not found:
                print(tmp)
                found = 1
        else:
            tmp = array[i]
            found = 0


def sum_of_numbers(n: int):
    # Сумма всех цифр числа
    if n < 10:
        return n
    return sum_of_numbers(n // 10) + n % 10


def products(n):
    # Все делители числа
    res = FastLL()
    for i in range(1, n):
        if not n % i:
            res.append(i)
    return res


def perfect_numbers_to(n):
    # Выводит все совершенные числа до указанного
    # Совершенные числа - числа, которые равны сумме всех своих делителей
    res = FastLL()
    for i in range(1, n):
        if i == products(i).summ:
            res.append(i)
    return res


def ants(n: int):
    temp = [bool(int(i)) for i in list(bin(n)[2:])]
    return all(temp) or not any(temp)


def nuggets(boxes: list, amount: int or float, depth=0, result=None, temp=None, answers=None):
    # Функция принимает на вход список чисел boxes и число amount
    # Возвращает все способы сложения чисел из boxes, дающие результат amount
    # Идея написания функции родилась во время просмотра видео про заказ 43 наггетсов
    # https://www.youtube.com/watch?v=vNTSugyS038
    if answers is None:
        answers = set()
    if not result:
        result = []
    if not temp:
        temp = amount
    boxes = sorted(boxes, reverse=True)
    if sum(result) == amount:
        answers.add(' '.join([str(i) for i in result]))
        return
    if len(boxes) == 0:
        return
    if temp == 0:
        return
    if len(boxes) == 1:
        if temp >= boxes[0]:
            result.append(boxes[0])
            nuggets(boxes, amount, depth=depth+1, result=result.copy(),
                    temp=temp-boxes[0], answers=answers)
        return
    if temp >= boxes[0]:
        result.append(boxes[0])
        nuggets(boxes, amount, depth=depth+1, result=result.copy(),
                temp=temp-boxes[0],answers=answers)
        nuggets(boxes[1:], amount, depth=depth+1, result=result.copy(),
                temp=temp-boxes[0], answers=answers)
    else:
        nuggets(boxes[1:], amount, depth=depth+1, result=result.copy(),
                temp=temp, answers=answers)
    nuggets(boxes[1:], amount, depth=depth+1, answers=answers)
    if depth == 0:
        return answers
    return
