

class StackMaxEffective:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.size() == 0:
            print('error')
        else:
            self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.size() == 0:
            print('None')
        else:
            print(max(self.items))


if __name__ == '__main__':

    stack = StackMaxEffective()
    n = int(input())
    for i in range(n):
        command = input()
        try:
            if command == 'get_max':
                stack.get_max()
            elif command == 'pop':
                stack.pop()
            elif command == 'get_max':
                stack.get_max()
            else:
                stack.push(int(command.split()[1]))
        except ValueError:
            print('Ошибка при вводе!!!')

'''
10
pop -> error
pop -> error
push 4
push -5
push 7
pop
pop
get_max -> 4
pop
get_max -> None
'''
