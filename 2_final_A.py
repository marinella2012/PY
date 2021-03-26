'''
Гоша реализовал структуру данных Дек, максимальный размер которого определяется
заданным числом. Методы push_back, push_front, pop_back, pop_front работали
корректно. Но, если в деке было много
элементов, программа работала очень долго. Дело в том, что не все операции
выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации нельзя использовать связный список.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
5000. Во второй строке записано число m — максимальный размер дека. Он не
превосходит 1000. В следующих n строках записана одна из команд:

push_back value – добавить элемент в конец дека. Если в деке уже находится
максимальное число элементов, вывести «error».

push_front value – добавить элемент в начало дека. Если в деке уже находится
максимальное число элементов, вывести «error».

pop_front – вывести первый элемент дека и удалить его. Если дек был пуст, то
вывести «error».

pop_back – вывести последний элемент дека и удалить его. Если дек был пуст,
то вывести «error».

value — целое число, по модулю не превосходящее 1000.
Формат вывода

Выведите результат выполнения каждой команды на отдельной строке. Для успешных
запросов push_back и push_front ничего выводить не надо.
'''


class Deque:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def pop_front(self):
        return self.items.pop()

    def pop_back(self):
        return self.items.pop(0)

    def push_front(self, item):
        return self.items.append(item)

    def push_back(self, item):
        return self.items.insert(0, item)


d = Deque()
n = int(input())
m = int(input())
for i in range(n):
    com = input().split(' ')
    if com == 'pop_front':
        d.pop_front()
    elif com == 'pop_back':
        d.pop_back()
    elif com == 'push_front':
        d.push_front(int(com[1]))
    d.push_back(int(com[1]))

print(d.items)
'''
4
4
push_front 861
push_front -819
pop_back
pop_back
'''