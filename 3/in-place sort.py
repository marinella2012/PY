def partition(arr, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] < pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quick_sort(arr, low, high, count):
    if count == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        '''
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        pivot = i + 1
        '''
        quick_sort(arr, low, pi-1, count)
        quick_sort(arr, pi+1, high, count)
        return arr


a = ['rita', 'anton', 'fekla']
b = len(a)
print(quick_sort(a, 0, b-1, b))
