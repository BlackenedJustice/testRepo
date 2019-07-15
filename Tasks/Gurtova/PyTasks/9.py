a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
temp1 = abs(a1-b1)
temp2 = abs(a2-b2)
if (temp1 == 1 and temp2 == 2) or (temp1 == 2 and temp2 == 1):
    print("Может")
else: print("Не может")