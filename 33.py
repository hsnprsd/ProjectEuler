import math

p, q = 1, 1

for y in range(10, 100):
	for x in range(10, y):
		a = x // 10
		b = y % 10
		if x * b == y * a and x % 10 == y // 10:
			p *= a
			q *= b

g = math.gcd(p, q)
p //= g
q //= g

print(q)