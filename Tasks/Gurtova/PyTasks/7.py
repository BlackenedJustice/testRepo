a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
temp1 = (a1-b1)%2
temp2 = (a2-b2)%2
if temp1 == temp2:
    print("YES")
else:
    print("NO")