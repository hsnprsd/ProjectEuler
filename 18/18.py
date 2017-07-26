f = open('in', 'r')
a = f.read().split('\n')
for i, d in enumerate(a):
	a[i] = list(map(int, d.split(' ')))

n = len(a)

dp = [[0 for i in range(n)] for i in range(n)]

for i in range(n - 1, -1, -1):
	for j in range(i + 1):
		dp[i][j] = a[i][j]
		if i < n - 1:
			dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[0][0])