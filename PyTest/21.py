n = int(input())
ans = (n+1)*n//2
for i in range(n-1):
	ans -= int(input())
print(ans)