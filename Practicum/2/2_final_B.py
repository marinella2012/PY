# 50278711


class Stack:
    def __init__(self):
        self.item = []

    def pop(self):
        try:
            return self.item.pop()
        except IndexError:
            raise IndexError('Стeк пуст')

    def push(self, value):
        self.item.append(value)


operations = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}


def do_operations():
    for element in seq:
        try:
            if element in operations.keys():
                second = stack.pop()
                first = stack.pop()
                stack.push(operations.get(element)(first, second))
            else:
                stack.push(int(element))
        except IndexError as error:
            print(error)
    print(stack.pop())


if __name__ == '__main__':
    seq = input().split()
    stack = Stack()
    do_operations()
