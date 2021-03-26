

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


'''def print_linked_list(node) -> None:
    while node:
        print(node.value)
        node = node.next_item'''


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


'''
def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next_item = head
        return new_node
    previous_node = get_node_by_index(head, index-1)
    new_node.next_item = previous_node.next_item
    previous_node.next_item = new_node
    return head '''


def solution(node, idx) -> Node:
    if idx == 0:
        head = node.next_item
        del(node)
        return head
    chosen_node = get_node_by_index(node, idx)
    previous_node = get_node_by_index(node, idx-1)
    previous_node.next_item = chosen_node.next_item
    del(chosen_node)
    return node


'''n4 = Node('x4')
n3 = Node('x3', n4)
n2 = Node('x2', n3)
n1 = Node('x1', n2)

print_linked_list(n1)

print()
solution(n1, 1)
print()
print_linked_list(n1)'''
