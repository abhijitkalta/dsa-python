#find all pairs whose sum is equal to given integer

l1 = [2, 4, 3, 5, 6, -2, 4, 7, 8 ,9]

def pairSum(l1, sum):
    res = []
    for i in range(len(l1)-1):
        for j in range(i+1, len(l1)):
            if l1[i] + l1[j] == sum:
                res.append('{}+{}'.format(l1[i], l1[j]))

    print(res)

pairSum(l1, 7)
