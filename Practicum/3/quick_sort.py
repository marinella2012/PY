

def quick_sort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop()

    items_greater = []
    items_lower = []

    for item in seq:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


if __name__ == '__main__':
    seq = [-4, -6, -2, -2, -4]
#    seq = [int(i) for i in input().split()]
    print(quick_sort(seq))
