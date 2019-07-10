def sgn(x):
    try:
        return int(x / abs(x))
    except ZeroDivisionError:
        return 0

x = float(input("Введите x: "))
print("sgn({}) = {}".format(x, sgn(x)))