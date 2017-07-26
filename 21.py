def d(n):
	s = 0
	i = 1
	while i * i <= n:
		if n % i == 0:
			s += i
			if n // i != i and i != 1:
				s += n // i
		i += 1
	return s

s = 0
for i in range(2, 10000):
	if d(d(i)) == i and d(i) != i:
		s += i

print(s)