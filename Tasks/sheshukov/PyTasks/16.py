a, b = map(int, input().split())
a -= a % 2
for i in range(a, b-1, -2):
    print(i)
