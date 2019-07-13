def fact(a):
    i = 1
    s = 1
    if a == 0:
        print(1)
    else:
        while i in range(a+1):
            s = s * i
            i = i + 1
        print(s)
