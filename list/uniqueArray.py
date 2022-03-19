arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
k = 4

def uniqueArray(arr, k):
    minVal = 0
    arr.sort()
    print('Sorted array:', arr)
    unfair = arr[-1]
    for i in range(len(arr)-k + 1):
        minVal = arr[i+k-1] - arr[i]
        print(minVal, arr[i+k -1], arr[i])
        if minVal < unfair:
            unfair = minVal
    return unfair

print(uniqueArray(arr, k))



