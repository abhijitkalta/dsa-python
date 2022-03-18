import ast
l1 = ast.literal_eval(input())
l2 = ast.literal_eval(input())

def permutationList(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        l1.sort()
        l2.sort()
        if l1 == l2:
            return True
        else:
            return False

print(permutationList(l1, l2))
