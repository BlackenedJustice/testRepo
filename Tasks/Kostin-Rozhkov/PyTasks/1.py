def fib(n):
    r = k = 1
    for i in range(n-1):
        r, k = k + r, r
    return r

print("N-ое число Фибоначчи равно {}".format(fib(int(input("Введите N: ")))))