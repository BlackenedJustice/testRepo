n = int(input())
s = 0
for i in range(1, n+1):
    s += i
for i in range(1, n):
    s -= int(input())

print(s)