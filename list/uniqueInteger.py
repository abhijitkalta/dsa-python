l1 = [1, 1, 2]
def lonelyinteger(l1):
    # Write your code here
    res = 0
    for i in range(len(l1)):
        if l1[i] in l1[0:i] or l1[i] in l1[i+1: ]:
            continue
        else:
            res = l1[i]
            return res
    return l1(-1)

print(lonelyinteger(l1))

