'''
В первой строке записано одно число — количество команд,
оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди,
он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:
    push x — добавить число x в очередь
    pop — удалить число из очереди и вывести на печать
    peek — напечатать первое число в очереди
    size — вернуть размер очереди
При превышении допустимого размера очереди нужно вывести «error».
При вызове операции pop или peek для пустой очереди нужно вывести «None».
'''


class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def get_node_by_index(node, index):
        while index:
            node = node.next_item
            index -= 1
        return node


class MyQueueSized:

    def __init__(self):
        self.head = None
        self.tail = None
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

    def put(self):
        pass

    def get(self):
        if self.is_empty():
            print('error')


if __name__ == '__main__':

    n = int(input())
    q = MyQueueSized()
    for i in range(n):
        com = input()
        try:
            if com == 'size':
                print(q.size)
            elif com == 'get':
                q.get()
            else:
                q.put(int(com.split(' ')[1]))
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
