n = 600851475143

mx = 0

i = 2
while i * i <= n:
	while n % i == 0:
		n //= i
		mx = i
	i += 1
if n > 1:
	mx = n

print(mx)