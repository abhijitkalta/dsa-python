#find missing number in array

l1 = [1, 2, 3, 4, 6]

def missingNumber(l1, total):
    expectedSum = total*(total+1)/2
    sum = 0
    for i in l1:
        sum+=i
    print('Missing number: {}'.format(expectedSum - sum))


missingNumber(l1, 6)
