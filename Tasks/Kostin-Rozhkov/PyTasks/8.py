print("Введите три числа: ")
x = len(set(input().split()))

str = "Число совпадающих чисел равно {}"
if x == 3:
    print(str.format(0))
elif x == 2:
    print(str.format(2))
elif x == 1:
    print(str.format(3))