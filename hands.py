# 49440229

import collections


def hands(k, line, score):
    dct = collections.Counter()
    for i in line:
        if i.isdigit() is True:
            dct[i] += 1
    for i in dct.items():
        if i[1] <= k * 2:
            score += 1
    return score


if __name__ == '__main__':
    k = int(input())
    line = []
    score = 0
    for j in range(4):
        j = input()
        line.append(j)
    line = ''.join(str(line))
    print(hands(k, line, score))
