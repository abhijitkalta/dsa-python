import ast
l1 = ast.literal_eval(input())
def uniqueElements(myList):
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] == myList[j]:
                print(i, j)
                return False
    return True

print(uniqueElements(l1))
