class Deque:
    def __init__(self, n):
        self.items = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.items == 0

    def push_front(self, item):
        self.items.append(item)

    def push_back(self, item):
        self.items.insert(0, item)

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        return self.items.pop()

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        return self.items.pop(0)

    def size(self):
        return len(self.items)


count = int(input())
n = int(input())
d = Deque(n)
for i in range(count):
    command = input()
    try:
        if command == 'pop_front':
            d.pop_front()
        elif command == 'pop_back':
            d.pop_back()
        elif command == 'push_back':
            try:
                d.push_back(int(command.split()[1]))
            except IndexError:
                print('error')
        else:
            try:
                d.push_front(int(command.split()[1]))
            except IndexError:
                print('error')
    except ValueError:
        print('Не знаю такой команды!!!')
print(d.items)
'''
'''
