m1 = [[1,2,3 ], [4, 5, 6], [7, 8, 9]]
res = []
print(m1)

for j in range(len(m1)):
    res.append([])
    for i in range(len(m1[j])):
        res[j].append(m1[i][j])
    res[j].reverse()

print(res)

rotated = list(zip(*m1[::-1]))
print(rotated)

res1 = []
for j in range(len(m1)):
    res1.append([])
    for i in range(len(m1[0])):
        res1[j].append(m1[-i-1][j])

print(res1)
