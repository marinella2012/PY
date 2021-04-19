# 49440300

def nearest_zero(n, houses):
    nearest_zero = [0 for i in range(n)]
    if (houses[0] == 0):
        nearest_zero[0] = 0
    else:
        nearest_zero[0] = n
    for i in range(1, n):
        nearest_zero[i] = nearest_zero[i - 1] + 1
        if (houses[i] == 0):
            nearest_zero[i] = 0
    if (houses[n - 1] == 0):
        nearest_zero[n - 1] = 0
    for i in range(n - 2, -1, -1):
        nearest_zero[i] = min(nearest_zero[i], nearest_zero[i + 1] + 1)
        if (houses[i] == 0):
            nearest_zero[i] = 0
    return nearest_zero


if __name__ == '__main__':
    n = int(input())
    houses = list(map(int, input().split()))
    print(nearest_zero(n, houses))
