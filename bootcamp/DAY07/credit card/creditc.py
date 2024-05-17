def sum_of_digits(num: int) -> int:
    return 1 + (num-1) % 9 


def doubled_dig(num: int) -> str:
    doubled_dig = ''
    for i in str(num)[::-2]:
        doubled_dig += str(sum_of_digits(int(i) * 2))
    return doubled_dig

def other_dig(num: int) -> str:
    return str(num)[-2::-2]


def sum_resulting(num) -> int:
    return sum(int(i) for i in (doubled_dig(num) + other_dig(num)))

def check_dig(num) -> int:
    return 10 - sum_resulting(num) % 10

print(doubled_dig(1789372997))
print(other_dig(1789372997))
print(doubled_dig(1789372997) + other_dig(1789372997))
print(sum_resulting(1789372997))
print(check_dig(1789372997))
