def fib(n):
    fib_1 = fib_2 = 1
    for i in range(n - 2):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib(int(input())))
