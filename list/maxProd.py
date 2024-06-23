import numpy as np

myArray = np.array([1, 20, 30, 44, 5, 56, 57,8, 9, 10, 31, 12,13, 14, 35, 16, 27,58, 19, 21])
maxProd = 0
res = 0
pairs = {}

for i in range(len(myArray) - 1):
    for j in range(i + 1, len(myArray)):
        res = myArray[i]*myArray[j]
        if res > maxProd:
            maxProd = res
            pairs = {
                    i: myArray[i],
                    j: myArray[j]
                    }

print(maxProd)
print(pairs)
