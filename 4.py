def is_pal(n):
	digits = []
	while n > 0:
		digits.append(n % 10)
		n //= 10
	t = len(digits)
	for i in range(t // 2):
		if digits[i] != digits[t - i - 1]:
			return False
	return True

mx = 0

for i in range(100, 1000):
	for j in range(100, 1000):
		if is_pal(i * j):
			mx = max(mx, i * j)

print(mx)