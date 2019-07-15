def fib(n):
    pre = cur = 1
    for i in range (1, n):
        pre += cur
        pre, cur = cur, pre
    return cur


for i in range (0, 10):
    print(fib(i), "\n")

