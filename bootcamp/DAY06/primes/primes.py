def is_prime(num: int) -> bool:
    count = 0
    for i in range(1, num // 2):
        if num % i == 0:
            count += 1
    return count == 2

def primes_under(limit: int) -> "list[int]":
    return [number for number in range(limit) if is_prime(number)]

print(primes_under(100))
        