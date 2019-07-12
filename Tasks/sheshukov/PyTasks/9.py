x1, y1, x2, y2 = map(int, input().split())

if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(y1 - y2) == 1 and abs(x1 - x2) == 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
