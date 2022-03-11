obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

obj3 = {
        "a": 2,
        "b": True,
        "c": 6
        }

def nestedEvenSum(obj, sum=0):
    for v in obj.values():
        if type(v) == dict:
            sum += nestedEvenSum(v)
        elif type(v) == int and v%2 ==0 :
            sum += v
    return sum

print(nestedEvenSum(obj2))


