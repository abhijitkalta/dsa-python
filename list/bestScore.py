#get first, second best scores

l1 = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]


def firstSecond(l1):
    l1.sort()
    print(l1[-1], l1[-2])

firstSecond(l1)
