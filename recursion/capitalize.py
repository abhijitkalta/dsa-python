import ast
l1 = ast.literal_eval(input('Input list of strings:'))
res = []
def capitalizeFirst(l1):
    if len(l1) == 1:
        res.append(l1[0].capitalize())
    else:
        res.append(l1[0].capitalize())
        return capitalizeFirst(l1[1:])
capitalizeFirst(l1)
print(res)
