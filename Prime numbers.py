# Python program to print prime numbers from 1 to N
# using Sieve of Eratosthenes

def sieve_of_eratosthenes(n):
	is_prime = [True] * (n+1)
	is_prime[0] = is_prime[1] = False
	for p in range(2, int(n**0.5)+1):
		if is_prime[p]:
			for i in range(p*p, n+1, p):
				is_prime[i] = False
	for i in range(2, n+1):
		if is_prime[i]:
			print(i, end=' ')


sieve_of_eratosthenes(100000000)

input()
