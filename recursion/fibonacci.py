import ast

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n-2) + fibonacci(n - 1)

n = ast.literal_eval(input("Enter your number: "))
assert n>=0 and int(n)==n, "Incorrect input"
for i in range(n):
    print(fibonacci(i), end=",")
