import ast

def sumOfDigits(n):
    assert n>0 and int(n)==n, "Incorrect input"
    if n%10 == n:
        return n
    else:
        res = n%10 + sumOfDigits(n//10)
        return res

n = ast.literal_eval(input("Enter any integer:"))
print(sumOfDigits(n))
