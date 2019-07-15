print ('введите числа')
a,b= (int(input())for i in range(2))
for i in range (1,b-a+1,1):
    print(i+a)
