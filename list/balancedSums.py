arr = [1, 2, 3, 3]

def balancedSum(arr):
    for i in range(1, len(arr)-1):
        if sum(arr[0:i]) == sum(arr[i+1:]):
            return True
    return False

def balancedSums(arr):
    left = 0
    right = sum(arr)
    for i in arr:
        right -= i
        if left == right:
            return "YES"
        left += i
    return "NO"

print(balancedSums(arr))
