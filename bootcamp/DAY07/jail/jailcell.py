def jail_problem(limit: int) :
    return [(n*n) for n in range(1, int(limit**0.5)+1)]
print(jail_problem(100))