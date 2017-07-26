l = []

def next_permutation(p):
	p = list(p)
	i = 2
	while sorted(p[9 - i:], reverse = True) == p[9 - i:]:
		i += 1
	idx = -1
	for j in range(9 - i + 1, 9):
		if p[j] > p[9 - i] and (idx == -1 or p[idx] > p[j]):
			idx = j
	p[9 - i], p[idx] = p[idx], p[9 - i]
	p[9 - i + 1:] = sorted(p[9 - i + 1:])
	return "".join(p)

def f(s):
	for i in range(1, 8):
		for j in range(1, 9 - i):
			k = 10 - i - j
			a = int(s[:i])
			b = int(s[i:i + j])
			c = int(s[i + j:])
			if a * b == c:
				l.append(c)

s = "123456789"
while 1 == 1:
	f(s)
	if s == "987654321":
		break
	s = next_permutation(s)

print(sum(set(l)))