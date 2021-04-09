

def get_numbers(elem1, elem2):
    return int(elem1 + elem2) > int(elem2 + elem1)


def big_digit(size, seq):
    for i in range(size):
        item_to_insert = seq[i]
        j = i
        while j > 0 and get_numbers(item_to_insert, seq[j-1]):
            seq[j] = seq[j-1]
            j -= 1
            seq[j] = item_to_insert
    return (''.join(str(i) for i in seq))


if __name__ == '__main__':
    size = int(input())
    seq = [i for i in input().split()]
    print(big_digit(size, seq))

'''
n = int(input())
A = []
for i in range(n):
    A.append(input())
 
for j in range(len(A) - 1, 0, -1):
    for i in range(0, j):
        if A[i + 1] + A[i] > A[i] + A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
 
print("".join(A))
'''
