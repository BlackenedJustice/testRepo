print ('введите координаты клеток')
x1, y1, x2, y2 = (int(input()) for i in range(4))
if (abs(x1-x2)==1 and  abs(y1-y2)==2) or  (abs(x1-x2)==2 and  abs(y1-y2)==1):
    ans='yes'
else:
    ans='no'
print(ans)
