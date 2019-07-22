print('enter the numbers')
a, b, c = (int(input()) for i in range(3))
if (a==b) and (a==c):
    ans=3
elif (a==b) or (a==c) or (b==c):
    ans=2
else:
    ans=0
print (ans)
