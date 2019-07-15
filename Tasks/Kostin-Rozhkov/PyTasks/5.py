print("Введите соответственно числа a, b, l, N: ")
a, b, l, n = map(int, input().split())
print("Искомая длина шнурка равна {}".format(2 * (l + (a + b) * n - b) - a))
