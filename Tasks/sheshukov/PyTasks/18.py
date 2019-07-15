def fact(k: int):
    for i in range (k - 1, 1, -1):
        k *= i
    return k


n = int(input())
print(fact(n))
