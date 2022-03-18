# find duplicate number from a list

l1 = [1, 1, 2, 2,2,  3, 4, 5]

def removeDuplicates(l1):
    res = []
    for i in l1:
        if i in l1[1:]:
            l1 = l1[1:]
            continue
        else:
            res.append(i)
            l1 = l1[1:]
    return res
print(removeDuplicates(l1))
