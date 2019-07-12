a,b=map(int,input().split())
a-=1-a%2
b+=1-b%2
for i in range(a,b-1,-2):
  print(i,end=' ')
print()
