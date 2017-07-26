def f(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return 1 + f(n // 2)
	return 1 + f(3 * n + 1)

mxt, mxi = 1, 1
for i in range(1, 1000000):
	t = f(i)
	if mxt < t:
		mxt = t
		mxi = i
print(mxi)