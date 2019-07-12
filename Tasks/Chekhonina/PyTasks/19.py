def sum_fact(n):
    sum = 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
        sum += fact
    return sum


print(sum_fact(int(input())))
