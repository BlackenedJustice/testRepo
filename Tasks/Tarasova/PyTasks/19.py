def sum_fact(n):
    factorial = 1
    sum = 0
    for i in range(1, n+1):
        factorial *= i
        sum += factorial
    return (sum)

a = int(input())
print(sum_fact(a))
