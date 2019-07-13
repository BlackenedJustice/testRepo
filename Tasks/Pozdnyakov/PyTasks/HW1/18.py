def fact(n):
  for i in range(1,n):
    n*=i
  return max(1,n)

n=int(input())
print(fact(n))
