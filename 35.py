n = 1000000

is_prime = [True for i in range(n)]
is_prime[0] = is_prime[1] = False
for i in range(2, n):
	if is_prime[i]:
		for j in range(i * i, n, i):
			is_prime[j] = False

def rotate(n):
	return n[1:] + n[0]

def is_cir_prime(n):
	n = str(n)
	l = len(n)
	while l > 0:
		if not is_prime[int(n)] or l > len(str(int(n))):
			return False
		n = rotate(n)
		l -= 1
	return True

t = 0
for i in range(2, n):
	if is_cir_prime(i):
		t += 1
print(t)