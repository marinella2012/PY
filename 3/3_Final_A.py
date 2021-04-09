
# 50404786

def b_search(seq, digit, left, right) -> int:

    mid = (left + right) // 2
    if digit == seq[mid]:
        return mid

    if right < left:
        return -1

    if seq[left] < seq[mid]:
        if seq[left] <= digit < seq[mid]:
            return b_search(seq, digit, left, mid - 1)
        else:
            return b_search(seq, digit, mid + 1, right)

    if seq[mid] < seq[right]:
        if seq[mid] < digit <= seq[right]:
            return b_search(seq, digit, mid + 1, right)
        else:
            return b_search(seq, digit, left, mid - 1)

    return -1

'''
if __name__ == '__main__':
    size = int(input())
    digit = int(input())
    seq = [int(i) for i in input().split()]
    print(b_search(seq, digit, left=0, right=size-1))
'''
a = [i for i in range(2000, 0, -1)]
print(a)

