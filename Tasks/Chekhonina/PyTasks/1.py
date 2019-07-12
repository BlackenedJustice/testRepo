fib_1 = fib_2 = 1
n = int(input()) - 2
for i in range(n):
    fib_1, fib_2 = fib_2, fib_1 + fib_2
print(fib_2)
