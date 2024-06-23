n = int(input())

def sumXor(n):
    res = []
    if n == 0:
        return 1
    else:
        return 2**(bin(n)[2:])
    for i in range(n):
        if n + i == n^i:
            res.append(i)
    return len(res)

print(sumXor(n))
