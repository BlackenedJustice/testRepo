def fact(n):
	if n == 0:
		return 1
	else:
		return fact(n - 1) * n

def sum_fact(n):
	x = []
	for i in range(1, n+1):
		x.append(fact(i))
	return sum(x)

print("Сумма всех факториалов до n равна {}".format(sum_fact(int(input("Введите n: "))))) 
