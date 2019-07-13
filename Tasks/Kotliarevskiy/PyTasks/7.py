print ('введите координаты клеток')
x1, y1, x2, y2 = (int(input()) for i in range(4))
if ((x1+y1)%2)==((x2+y2)%2):
    ans='yes'
else:
    ans='no'
print(ans)
