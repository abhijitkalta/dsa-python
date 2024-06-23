import ast
def gcd(n, m):
    if n%m == 0:
        return n
    else:
        r = n%m
        return gcd(m, r)

print(gcd(18, 48))
