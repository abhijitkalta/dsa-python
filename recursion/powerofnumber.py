import ast

def powerOfNumber(n, m):
    if m == 0:
        return 1
    else:
        return n * powerOfNumber(n, m - 1)

print(powerOfNumber(4, 3))
