t = [0 for i in range(1001)]

for i in range(1, 1000):
	for j in range(i, 1000):
		for k in range(j	, 1000):
			if i + j + k <= 1000 and i * i + j * j == k * k:
				t[i + j + k] += 1

mx = 0
for i in range(1001):
	if t[i] > t[mx]:
		mx = i
print(mx)