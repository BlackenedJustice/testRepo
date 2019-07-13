n = int(input())
i = 1
s = 0
while i in range (n + 1):
    s = s + i
    i = i + 1
i = 1
while i in range (n):
    a = int(input())
    s = s - a
    i = i + 1
print(s)
