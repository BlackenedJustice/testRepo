N = int(input())
sum = N*(N+1)//2
for i in range(N-1):
    sum -= int(input())
print(sum)