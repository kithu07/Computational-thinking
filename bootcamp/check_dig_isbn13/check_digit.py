"""Multiply each of the first 12 digits by 1 or 3, alternating as you move from left to right, and sum the results.

Divide the sum by 10.

Subtract the remainder (not the quotient) from 10.

If the result is 10, use the number 0"""

def digitsum_modified_no(code: str) -> int:
    sum_digits = 0
    for i in range(0, len(code), 2):
        sum_digits += int(code[i])
    for i in range(1, len(code), 2):
        sum_digits += int(code[i]) * 3
    return sum_digits
 
def check_digit(code: str) -> int:
    sum = digitsum_modified_no(code)
    check_digit = 10 - sum % 10
    if check_digit == 10:
        return 0
    return check_digit

print(check_digit("978059652068"))