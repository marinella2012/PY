# 50171720


class Stack:
    def __init__(self):
        self.item = []

    def summation(self):
        a, b = self.item.pop(), self.item.pop()
        self.item.append(int(b) + int(a))

    def subtraction(self):
        a, b = self.item.pop(), self.item.pop()
        self.item.append(int(b) - int(a))

    def multiplication(self):
        a, b = self.item.pop(), self.item.pop()
        self.item.append(int(b) * int(a))

    def integer_division(self):
        a, b = self.item.pop(), self.item.pop()
        self.item.append(int(b) // int(a))

    operation = {
        '+': summation,
        '-': subtraction,
        '*': multiplication,
        '/': integer_division
    }

    def parsing_postfix_notation(self, postfix_notation):
        for element in postfix_notation:
            if element not in self.operation:
                self.item.append(element)
            else:
                self.operation[element](self)
        return self.item[-1]


if __name__ == '__main__':

    notation = Stack()
    print(notation.parsing_postfix_notation(input().split()))

'''
operation_sign = {
    '+': lambda x, y: y+x,
    ...
}
ТОгда результат вычислений можно было бы получить, таким образом:
stack.append(operation_sign[sign](stack.pop(), stack.pop()))
'''
