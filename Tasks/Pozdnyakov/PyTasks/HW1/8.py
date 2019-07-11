a,b,c=map(int,input().split())
if a==b:
  if a==c:
    print(3)
  else:
    print(2)
else:
  if a==c:
    print(2)
  else:
    if b==c:
      print(2)
    else:
      print(0)
