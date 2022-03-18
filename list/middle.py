l1 = [1,2,3,4]

res = []
for i in range(len(l1)):
    if i == 0 or i == len(l1) - 1:
        continue
    else:
        res.append(l1[i])

print(res)
