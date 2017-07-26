prod = 1
for i in range(1, 101):
	prod *= i

s = 0
while prod > 0:
	s += prod % 10
	prod //= 10

print(s)