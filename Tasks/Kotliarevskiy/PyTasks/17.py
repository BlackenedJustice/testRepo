print ('введите числа')
a,b= (int(input())for i in range(2))
a=a-1+(a%2)
for i in range (0,a-b+1,2):
    print(a-i)
