print("Введите размер лестницы n: ")
n = int(input())
for i in range(1, n + 1):
	print(str(list(range(1, i + 1)))[1:-1:3])
