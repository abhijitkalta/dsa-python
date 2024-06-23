def reversed(n):
    if len(n)==1:
        return n[0]
    else:
        return n[-1] + reversed(n[0: -1])

print(reversed('python'))
