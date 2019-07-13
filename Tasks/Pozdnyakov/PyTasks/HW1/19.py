def sum_fact(n):
  for i in range(n-1,0,-1):
    n=(n+1)*i
  return max(1,n)

n=int(input())
print(sum_fact(n))
