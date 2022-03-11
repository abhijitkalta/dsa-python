import ast
in1 = ast.literal_eval(input("Enter list:"))

res = []
def flatten(in1):
    if len(in1)==1 and not isinstance(in1[0], list):
        res.append(in1[0])
        return res
    else:
        if isinstance(in1[0], list):
            if len(in1)==1:
                flatten(in1[0])
            else:
                flatten(in1[0])
                return flatten(in1[1:])
        else:
            res.append(in1[0])
            return flatten(in1[1: ])


flatten(in1)
print(res)



