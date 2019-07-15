def new_sgn(x):
    return 0 if x == 0 else x / abs(x)


print(new_sgn(int(input())))
