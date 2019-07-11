print("Введите числа A и B: ")
a, b = map(int, input().split())
print("Все нечетные числа от A до B включительно, в убывающем порядке: {}".format(str(list(range(a + a % 2 - 1, b - b % 2, -2)))))
