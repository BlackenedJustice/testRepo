print("Введите числа A и B: ")
a, b = map(int, input().split())
print("Все числа от A до B включительно: {}".format(str(list(range(a, b + 1)))[1:-1]))
