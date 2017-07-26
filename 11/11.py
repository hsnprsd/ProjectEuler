n = 20

f = open('in', 'r')
a = list(map(int, f.read().replace('\n', ' ').split(' ')[:-1]))

def get(x, y):
	return a[x * n + y]

def is_valid(x, y):
	return x >= 0 and x < n and y >= 0 and y < n

def f(dx, dy):
	global n
	mx = 0
	for i in range(n):
		for j in range(n):
			prod = 1
			for k in range(4):
				x = dx * k + i
				y = dy * k + j
				if is_valid(x, y):
					prod *= get(x, y)
				else:
					prod = 0
			mx = max(mx, prod)
	return mx

mx = max(f(1, 0), f(0, 1), f(1, 1), f(1, -1))
print(mx)