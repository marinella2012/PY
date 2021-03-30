# fib

def fib(mod):
    a, b = 1, 1

    while True:
        yield a
        a, b = b, (a + b) % mod


n, k = map(int, input().split(' '))
g = fib(mod=10**k)
answer = next(g)

for _ in range(n):
    answer = next(g)
print(answer)


# linked_list.py
# 1 -> 3 -> 5 -> 7 -> 9
# 9 -> 7 -> 5 -> 3 -> 1

class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value




def print_linked_list(node: Node):
    while node:
        print(node.value, end=' -> ')
        node = node.next

    print()

def reverse_linked_list(node: Node):
    prev, current = None, node

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(7)
    n5 = Node(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print_linked_list(n1)
    print()

    n_reversed = reverse_linked_list(n1)
    print_linked_list(n_reversed)
    print()

    print_linked_list(n1)

# alg.py
from linked_list import Node, reverse_linked_list, print_linked_list

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

n1_ = Node(5)
n2_ = Node(6)
n3_ = Node(7)
n4_ = Node(8)

n1_.next = n2_
n2_.next = n3_
n3_.next = n4_


# 1->2->3->4->5->6
# 5->6->7->8
# 1->2->9->1->3->4
# 123456 + 5678 = 129134

# 9 -> 9 -> 9
# 1 ->
# 1 -> 0 -> 0 -> 0

def linked_lists_sum(node1, node2):
    node1 = reverse_linked_list(node1)
    node2 = reverse_linked_list(node2)

    sum_ = node1.value + node2.value
    flag = sum_ // 10
    head = Node((sum_) % 10)  # 4 ->

    t_node1, t_node2 = node1.next, node2.next
    t_node = head

    while t_node1 or t_node2:
        sum_ = flag
        if t_node1:
            sum_ += t_node1.value
            t_node1 = t_node1.next
        if t_node2:
            sum_ += t_node2.value
            t_node2 = t_node2.next
        flag = sum_ // 10

        t_node.next = Node(sum_ % 10)
        t_node = t_node.next

    if flag:
        t_node.next = Node(flag)

    node1 = reverse_linked_list(node1)
    node2 = reverse_linked_list(node2)
    head = reverse_linked_list(head)

    print_linked_list(node1)
    print_linked_list(node2)
    print_linked_list(head)


if __name__ == '__main__':
    linked_lists_sum(n1, n1_)
