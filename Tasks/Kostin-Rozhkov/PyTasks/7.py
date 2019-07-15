print("Введите координаты (c1, r1) первой клетки и координаты (c2, r2) второй: ")
a, b, c, d = map(int, input().split())

if (a + b - c - d) % 2 == 0:
    print("YES")
else:
    print("NO")