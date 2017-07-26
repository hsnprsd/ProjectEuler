s = ""

i = 1
while len(s) < 1000000:
	s += str(i)
	i += 1

def get(idx):
	idx -= 1
	global s
	return int(s[idx])

print(get(1) * get(10) * get(100) * get(1000) * get(10000) * get(100000) * get(1000000))