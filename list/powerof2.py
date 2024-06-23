from math import log
n = int(input())
def powerOf2(n):
    count = 0
    while n != 1:
        k = log(n, 2)
        if k != int(k):
            for i in range(n, 0, -1):
                j = 0
                if int(log(i, 2)) == log(i, 2):
                    j = i
                    break
            n = n - j
            count += 1
        else:
            n = n//2
            count += 1
    if count%2 == 1:
        return 'Louise'
    else:
        return 'Richard'

def power2(n):
    count = 0
    while n!=1:
        k = log(n,2)
        if k != int(k):
            n = n - pow(2, int(log(n,2)))
        else:
            n = n//2
        count += 1
    if count%2 == 1:
        return "Lousie"
    else:
        return 'Richard'



print(power2(n))


