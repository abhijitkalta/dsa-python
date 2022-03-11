import ast

res = []
def decToBin(n):
    assert int(n)==n, "enter an integer"
    if n < 2:
        return res.append(1)
    else:
        remainder = n%2
        n = n//2
        res.append(remainder)
        return decToBin(n)
n = ast.literal_eval(input("Enter any number: "))
decToBin(n)
res.reverse()
print("".join(map(str, res)))
