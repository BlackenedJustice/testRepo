def sum_fact(n):
	sum = 0
	fact = 1
	for i in range(1,n+1):
		fact *= i
		sum = sum + fact
	return sum