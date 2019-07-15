a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a = abs(a1 - a2)
b = abs(b1 - b2)
if a == 1 and b == 2 or a == 2 and b == 1:
    print('YES')
else:
    print('NO')
