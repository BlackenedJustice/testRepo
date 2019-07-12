def fact(n):
    rez = 1
    for i in range(2, n + 1):
        rez *= i
    return rez


print(fact(int(input())))

