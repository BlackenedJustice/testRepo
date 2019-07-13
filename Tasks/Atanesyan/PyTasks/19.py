def sum_fact(a):
    i = 1
    f = 1
    s = 0
    if a == 0:
        print(s)
    else:
        while i in range(a + 1):
            f = f * i
            s = s + f
            i = i + 1
        print(s)
    
