def sum_fact(k: int):
    res = 1
    for i in range(k, 1, -1):
        res = res * i + 1
    return res


print(sum_fact(int(input())))

