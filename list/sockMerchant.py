def sockMerchant(n, ar):
    # Write your code here
    res = 0
    ar.sort()
    i = 0
    while i <= len(ar)-2:
        count = 1
        for j in range(i+1, len(ar)):
            if ar[i] != ar[j]:
                # ar = ar[j:]
                i = j
                break
            else:
                count += 1
                i += 1
        res += count//2
    return res
print(sockMerchant(10,[1,1,3,1,2,1,3,3,3,3]))
