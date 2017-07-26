def num_of_divisors(n):
	t = 0
	i = 1
	while i * i <= n:
		if n % i == 0:
			t += 1
			if i != n // i:
				t += 1
		i += 1
	return t

i = 1
while num_of_divisors(i * (i + 1) // 2) <= 500:
	i += 1

print(i * (i + 1) // 2)