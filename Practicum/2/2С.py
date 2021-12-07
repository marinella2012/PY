

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


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
