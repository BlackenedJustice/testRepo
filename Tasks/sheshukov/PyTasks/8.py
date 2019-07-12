a, b, c = map(int, input().split())

if (a, b, c) == (c, a, b):
    print(3)
else:
    if a == b or b == c or a == c:
        print(2)
    else:
        print(0)
