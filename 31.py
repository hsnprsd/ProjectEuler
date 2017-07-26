p = [1, 2, 5, 10, 20, 50, 100, 200]

dp = [[0 for i in range(len(p) + 1)] for i in range(201)]

for i in range(len(p) + 1):
	dp[0][i] = 1
for i in range(1, 201):
	for j in range(1, len(p) + 1):
		for k in range(0, 201):
			if i >= k * p[j - 1]:
				dp[i][j] += dp[i - k * p[j - 1]][j - 1]

print(dp[200][len(p)])