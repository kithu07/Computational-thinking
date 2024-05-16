def sum_of_digits(num: int) -> int:
    # d = num % 9
    # return 9 if d is 0 else d
    return 1 + (num-1) % 9 
print(sum_of_digits(279))

