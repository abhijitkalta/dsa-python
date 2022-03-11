obj = {
        "num": 1,
        "test": [],
        "data": {
            "val": 4,
            "info": {
                "isRight": "Hello",
                "random": 66
                }
            }
        }


def stringifyNumbers(obj):
    for k in obj:
        if isinstance(obj[k], dict):
            stringifyNumbers(obj[k])
        else:
            if type(obj[k]) == int:
                obj[k] = str(obj[k])

print("*", obj)
stringifyNumbers(obj)
print(obj)

res = []
def collectStrings(obj):
    for i in obj:
        if isinstance(obj[i], dict):
            collectStrings(obj[i])
        else:
            if type(obj[i]) == str:
                res.append(obj[i])
collectStrings(obj)
print(res)
