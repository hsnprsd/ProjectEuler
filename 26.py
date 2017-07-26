def f(n):
	t = {}
	r, i = 1, 0
	while not r in t:
		t[r] = i
		r = (r % n) * 10
		i += 1
	return i - t[r]

a = 2
for d in range(3, 1000):
	if f(a) < f(d):
		a = d
print(a)
