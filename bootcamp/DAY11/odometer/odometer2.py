def is_ascending(n):
    if n < 10:
        return True
    elif (n // 10) % 10 > n % 10:
        return False
    else:
        return is_ascending(n // 10)

def limits(n):
    DIGITS = "123456789"
    size = len(str(n))
    return int(DIGITS[:size]), int(DIGITS[-size:]) 

def possible_readings(n, size):
    for limit in range(9, 0, -1):
        for digit in range(size - 1, limit):
            