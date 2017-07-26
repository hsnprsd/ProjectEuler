def v(n):
	s = 0
	for c in n:
		s += ord(c) - ord('A') + 1
	return s

f = open('in', 'r')
names = f.read().replace('"', '').replace('\n', '').split(',')

names.sort()

s = 0
for i, n in enumerate(names):
	s += v(n) * (i + 1)
print(s)