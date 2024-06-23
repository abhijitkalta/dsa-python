def reversed(n):
    if len(n)==1:
        return n[0]
    else:
        res = n[-1] + reversed(n[0: -1])
        return res
n = str(input("Enter any string: "))
res = reversed(n)
if res == n:
    print(True)
else:
    print(False)
