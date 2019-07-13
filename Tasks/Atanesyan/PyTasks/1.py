def fib(a):
    sum = prev = 1
    for i in range(a-1):
        sum += prev
        prev = sum - prev
    print(sum)
