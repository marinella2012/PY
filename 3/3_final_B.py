
# 50517298


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j][1] < pivot[1]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        if arr[j][1] == pivot[1]:

            if arr[j][2] < pivot[2]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

            if arr[j][2] == pivot[2]:
                if arr[j][0] < pivot[0]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low, high):
    if low >= high:
        return

    pi = partition(arr, low, high)

    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi+1, high)
    return


if __name__ == '__main__':
    count = int(input())
    info = []
    for _ in range(count):
        name, point, penalty = input().split()
        info.append((name, -int(point), int(penalty)))
    quick_sort(info, 0, count-1)
    print(*[info[i][0] for i in range(count)], sep='\n')
