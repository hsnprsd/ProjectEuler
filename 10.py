n = 2000000

is_prime = [True] * n

ans = 0

is_prime[0] = is_prime[1] = False
for i in range(2, n):
	if is_prime[i]:
		for j in range(2 * i, n, i):
			is_prime[j] = False
		ans += i

print(ans)