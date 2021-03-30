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

# 50159756


class Deque:
    def __init__(self, n):
        self.items = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, item):
        if self.size >= self.max_n:
            raise IndexError('error')
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, item):
        if self.size >= self.max_n:
            raise IndexError('error')
        self.head = (self.head - 1) % self.max_n
        self.items[self.head] = item
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('error')
        x = self.items[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            raise IndexError('error')
        self.tail = (self.tail - 1) % self.max_n
        x = self.items[self.tail]
        self.size -= 1
        return x


if __name__ == '__main__':
    count = int(input())
    n = int(input())
    d = Deque(n)
    commands = []
    for _ in range(count):
        commands.append(input())
    for line in commands:
        command, *args = line.split()
        try:
            if command == 'pop_front':
                print(d.pop_front())
            elif command == 'pop_back':
                print(d.pop_back())
            elif command == 'push_back':
                d.push_back(*args)
            elif command == 'push_front':
                d.push_front(*args)
            else:
                print('Не знаю такой команды!')
        except IndexError as error:
            print(error)
'''
7
10
push_front -855
push_front 720
pop_back
pop_back
push_back 844
pop_back
push_back 823
'''
