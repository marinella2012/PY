

def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(0, (k - 1)):
        for amount in range(1, counted_values[value]):
            array[index] = value
            index += 1
    return array


array = ''
k = int(input())
print(counting_sort(array, k))
