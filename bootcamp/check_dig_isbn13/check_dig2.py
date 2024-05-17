HYPHEN = '-'
def clean(isbn):
    return [int(ch) for ch in isbn if ch != HYPHEN]
def check_isbn(isbn):
    return check_digit(isbn[::-1]) == int(isbn[-1])
def check_digit(isbn):
    weights = [1, 3] * 6
    check_digit = sum([a * b for (a, b) in zip(weights, clean(isbn))]) % 10
    return 0 if check_digit == 0 else 10 - check_digit