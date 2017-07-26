def is_prime(n):
	if n < 2:
		return False
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def f(a, b):
	n = 0
	while is_prime(n * n + a * n + b):
		n += 1
	return n

mx, prod = -1, 0
for a in range(-999, 1000):
	for b in range(-999, 1000):
		if f(a, b) > mx:
			mx = f(a, b)
			prod = a * b
print(prod)