def fib(n):
    first = second = 1
    while n-2 > 0:
        second, first = first, first + second
        n = n-1
    return first