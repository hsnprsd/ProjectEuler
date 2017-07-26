oned = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
btat = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
twod = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def int_to_str(n):
	if n == 1000:
		return 'one thousand'
	if n < 10:
		return oned[n]
	if n < 20:
		return btat[n - 10]
	if n < 100:
		if n % 10 == 0:
			return twod[n // 10 - 1]
		return twod[n // 10 - 1] + ' ' + oned[n % 10]
	if n % 100 == 0:
		return oned[n // 100] + ' hundred'
	if (n // 10) % 10 == 0:
		return oned[n // 100] + ' hundred and ' + int_to_str(n % 10)
	return oned[n // 100] + ' hundred and ' + int_to_str(n % 100)

print(int_to_str(200))

ans = 0
for i in range(1, 1001):
	ans += len(int_to_str(i).replace(' ', ''))
print(ans)