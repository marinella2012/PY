

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_linked_list(node) -> None:
    while node:
        print(node.value)
        node = node.next_item


def solution(node, elem) -> int:
    idx = 0
    try:
        while node.value != elem:
            node = node.next_item
            idx += 1
    except AttributeError:
        idx = -1
    return idx


'''
n4 = Node('x4')
n3 = Node('x3', n4)
n2 = Node('x2', n3)
n1 = Node('x1', n2)

print_linked_list(n1)

print()
print(solution(n1, 'x5'))'''
