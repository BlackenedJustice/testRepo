def fib(n):
  x=1
  y=1
  for i in range(n-1):
    x,y=y,x+y
  return y

n=int(input())
print(fib(n))
