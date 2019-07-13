v = int(input())
t = int(input())
if v >= 0:
    print ((v * t) % 109)
else:
    c = abs(v * t) // 109
    print(109 * (c + 1) + v * t)
