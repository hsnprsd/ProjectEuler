def fact(n):
	p = 1
	for i in range(2, n + 1):
		p *= i
	return p

def f(n):
	s = 0
	while n > 0:
		s += fact(n % 10)
		n //= 10
	return s

s = 0
for i in range(10, 10000000):
	if f(i) == i:
		s += i

print(s)