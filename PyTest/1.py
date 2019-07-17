def fib(n):
	x, prev = 1, 0
	for i in range (n):
		x, prev = prev+x, x
	return x