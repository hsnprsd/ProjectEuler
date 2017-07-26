def is_prime(n):
	if n < 2:
		return False
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def is_trunc_prime(n):
	m = n
	while m > 0:
		if not is_prime(m):
			return False
		m //= 10
	m = n
	while 1 == 1:
		if not is_prime(m):
			return False
		if len(str(m)) == 1:
			break
		m = int(str(m)[1:])
	return True

t = 11
n = 11
s = 0
while t > 0:
	if is_trunc_prime(n):
		s += n
		t -= 1
	n += 1

print(s)