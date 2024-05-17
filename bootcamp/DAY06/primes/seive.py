def SieveOfEratosthenes(n1,n2):
	prime = [True for i in range(n2+1)]
	p = 2
	while (p * p <= n2):
		if prime[p]:
			for i in range(p*p, n2+1, p):
				prime[i] = False
		p += 1
	return  [p for p in range(n1,n2+1) if prime[p]]
    
print(SieveOfEratosthenes(100,1000))
