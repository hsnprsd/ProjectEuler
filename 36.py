def is_pal(s):
	if s == s[-1:0:-1] + s[0]:
		return True
	return False

def to_binary(x):
	s = ""
	while x > 0:
		s += str(x % 2)
		x //= 2
	return s

s = 0
for i in range(1, 1000000):
	if is_pal(str(i)) and is_pal(to_binary(i)):
		s += i
print(s)