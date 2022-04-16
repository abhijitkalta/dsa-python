s = input()
def pangram(s):
    s = set(s.lower())
    print(s, len(s))
    if len(s) == 27:
        return 'pangram'
    else:
        return 'not pangram'

print(pangram(s))
