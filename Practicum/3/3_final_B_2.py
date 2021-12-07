
#


class Person:
    def __init__(self, name, point, penalty):
        self.name = name
        self.point = -int(point)
        self.penalty = int(penalty)

    def __gt__(self, other):
        if self.point == other.point:
            if self.penalty == other.penalty:
                return self.name > other.name
            return self.penalty > other.penalty
        return self.point > other.point

#    def __str__(self):
#        return self.name


def partition(arr, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] < pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


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
    person = Person(name=None, point=0, penalty=0)
    for _ in range(count):
        info.append(Person(*input().split()))
    quick_sort(info, 0, count-1)
    print(*[person.name for person in info], sep='\n')
