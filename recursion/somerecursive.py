def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    if len(arr)==1:
        return cb(arr[0])
    else:
        if cb(arr[0])==True:
            return True
        else:
            return someRecursive(arr[1: ], cb)


print(someRecursive([ 2,  4], isOdd))
