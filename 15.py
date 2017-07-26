ans = 1
for i in range(1, 41):
	ans *= i
for i in range(1, 21):
	ans //= i * i
print(ans)