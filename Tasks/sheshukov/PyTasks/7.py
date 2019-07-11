x1, x2, y1, y2 = int(input()), int(input()), int(input()), int(input())

if ((x1 % 2 + x2 % 2) % 2) == ((y1 % 2 + y2 % 2) % 2):
    print("YES")
else:
    print("NO")