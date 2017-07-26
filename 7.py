def is_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

i, t = 2, 0
while t < 10001:
	if is_prime(i):
		t += 1
	i += 1

print(i - 1)	