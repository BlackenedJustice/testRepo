x_1, y_1, x_2, y_2 = map(int, input().split())
if abs(x_1 - x_2) == 1 and abs(y_1 - y_2) == 2 or abs(x_1 - x_2) == 2 and abs(y_1 - y_2) == 1:
    print('YES')
else:
    print('NO')
