n = int(input())
def flippingBits(n):
    b = bin(n)[2:]
    print(b)
    # res = [(lambda x: 1 if int(x) ==0 else 0)(x) for x in b]
    res = [1 if int(x) == 0 else 0 for x in b]
    print(str(res))


flippingBits(n)
