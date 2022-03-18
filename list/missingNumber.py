import array as arr

n1 = arr.array('i', [1, 2, 4, 5, 7, 9, 11])
res = []
for i in range(n1[len(n1) - 1]):
    j = i + 1
    if j not in n1:
        res.append(j)
res = ','.join(map(str, res))
print("Missing numbers: {}".format(res))
