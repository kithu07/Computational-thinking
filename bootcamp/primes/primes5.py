def generate_primes(limit):
    def is_prime(num):
        factor = 7
        while factor * factor <= num:
            if num % factor ==0:
                return False
            factor += 2
        return True
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    for n in range(30, limit, 30):
        for step in [1,7,11,13,17,19,23,29]:
            if is_prime(n + step):
                primes.append(n + step)
    return [prime for prime in primes if prime<1000]
print(generate_primes(1000))

