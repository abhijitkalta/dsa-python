# calculate sum of diagonal elements

l1 = [[1,2,3], [4,5,6],[7,8,9]]

def sumDiagonal(l1):
    sum = 0
    for j in range(len(l1)):
        sum += l1[j][j]
    return sum

sum = sumDiagonal(l1)
print(sum)
