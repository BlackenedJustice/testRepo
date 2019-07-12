n = int(input())
sum = (1 + n) * n * 0.5
for i in range (n - 1):
    sum -= int(input())
print(int(sum))
