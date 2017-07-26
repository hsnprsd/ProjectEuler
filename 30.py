def f(n):
	s = 0
	while n > 0:
		s += (n % 10) ** 5
		n //= 10
	return s

s = 0
for i in range(10, 1000000):
	if f(i) == i:
		s += i
print(s)