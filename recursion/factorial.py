import ast
def factorial(n):
    assert n>=0 and int(n)==n, "Incorrect input"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

n = ast.literal_eval(input())
print(factorial(n))
