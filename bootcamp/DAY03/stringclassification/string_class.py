def is_strictly_ascending(charset: str) -> bool:
    for i in range(1, len(charset)):
        if charset[i-1] > charset[i]:
            return False
    return True
#a,d,p,v,x

def is_strictly_descending(charset: str) -> bool:
    for i in range(len(charset)-1):
        if charset[i] < charset[i + 1]:
            return False
    return True

def has_peak(charset: str) -> int:
    count=0
    for i in range(1, len(charset)):
        if i-1 < i > i+1:
            count += 1
    return count

def has_valley(charset: str) -> int:
    count=0
    for i in range(1, len(charset)):
        if i-1 > i < i+1:
            count += 1
    return count

def classify(charset: str) -> str:
    if is_strictly_ascending(charset):
        return "A"
    elif is_strictly_descending(charset):
        return "D"
    elif has_peak(charset) == 1:
        return "P"
    elif has_valley(charset) == 1:
        return "V"
    else:
        return "X"
print(classify("Hi"),classify("to"))


