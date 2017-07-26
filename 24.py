def next_permutation(p):
	i = 2
	while sorted(p[10 - i:], reverse = True) == p[10 - i:]:
		i += 1
	idx = -1
	for j in range(10 - i + 1, 10):
		if p[j] > p[10 - i] and (idx == -1 or p[idx] > p[j]):
			idx = j
	p[10 - i], p[idx] = p[idx], p[10 - i]
	p[10 - i + 1:] = sorted(p[10 - i + 1:])
	return p

p = range(10)
for i in range(1, 1000000):
	p = next_permutation(p)

print(''.join(map(str, p)))