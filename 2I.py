

class MyQueueSized:

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            print(None)
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            print(x)

    def peek(self):
        if self.is_empty():
            print(None)
        else:
            print(self.queue[self.head])


if __name__ == '__main__':
    count = int(input())
    n = int(input())
    q = MyQueueSized(n)
    for i in range(count):
        com = input()
        try:
            if com == 'peek':
                q.peek()
            elif com == 'size':
                print(q.size)
            elif com == 'pop':
                q.pop()
            else:
                q.push(int(com.split(' ')[1]))
        except ValueError:
            print('Ошибка при вводе!!!')
#    print(q.queue)


'''
-->:
8
2
peek -> None
push 5
push 2
peek -> 5
size -> 2
size -> 2
push 1 -> error
size -> 2
'''
