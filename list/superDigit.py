def superDigit(n):
    sum = 0
    if n//10 == 0:
        return n
    else:
        sum = n%10 + superDigit(n//10)
        return superDigit(sum)

s1 = str(input())
n = s1.split()[0]
k = int(s1.split()[1])
p = n*k
print(superDigit(int(p)))

def supDigit(n, k):
    if len(n) == 1 and k == 1:
        return n
    else:
        print(list(map(int, n))*k)
        total = str(sum([int(d) for d in n] * k))
        return supDigit(total, 1)
print("Super digit: {}".format(supDigit(n, k)))
