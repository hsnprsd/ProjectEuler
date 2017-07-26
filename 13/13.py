f = open('in', 'r')

ans = 0
for i in range(100):
	x = int(f.readline())
	ans += x
print(str(ans)[:10])