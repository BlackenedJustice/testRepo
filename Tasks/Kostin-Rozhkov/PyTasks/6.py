def sgn(x):
    if x != 0:
        return int(x / abs(x))
    return 0

x = float(input("Введите x: "))
print("sgn({}) = {}".format(x, sgn(x)))
