def classify_strings(strings):
    if len(strings) <= 1:
        return 'X'
    if isascending(strings):
        return 'A'
    elif isdescending(strings):
        return 'D'
    elif no_of_peak(strings) == 1 and no_of_valleys(strings) == 0:
        return 'P'
    elif no_of_peak(strings) == 0 and no_of_valleys(strings) == 1:
        return 'v'
    else:
        return 'X'
    
def isascending(strings):
    return all(a < b  for a,b in zip(strings,strings[1:]))

def isdescending(strings):
    return all(a > b  for a,b in zip(strings,strings[1:]))

def no_of_peak(strings):
    return sum(a < b > c for a, b, c in zip(strings, strings[1:], strings[2:]))


def no_of_valleys(strings):
    return sum(a > b < c for a, b, c in zip(strings, strings[1:], strings[2:]))

print(classify_strings("1234321"))
