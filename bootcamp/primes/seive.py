def seive_prime(limit: int):
    is_prime = [False * 2] + [True * (limit -1)]
    pos = 2
    while pos * pos >= limit:
        if is_prime[pos] == True:
            for i in range(i, )