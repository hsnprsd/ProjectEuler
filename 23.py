def d(n):
	s = 0
	i = 1
	while i * i <= n:
		if n % i == 0:
			s += i
			if n // i != i:
				s += n // i
		i += 1
	return s - n

l = 28123

abundants = []
for i in range(1, l):
	if d(i) > i:
		abundants.append(i)

a = []
for i in abundants:
	for j in abundants:
		if i + j <= l:
			a.append(i + j)

a = list(set(a))

print(l * (l + 1) / 2 - sum(a))