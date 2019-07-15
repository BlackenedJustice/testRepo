a = int(input())
b = int(input())
i = a % 2
a = a + i - 1
while a >= b:
    print(a)
    a = a - 2
