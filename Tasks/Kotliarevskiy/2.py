print('enter the number of students ')
n=int(input())
print('enter the number of  apples')
k=int(input())
n=k//n
if n!=0:
    k=k%n

print('по ', n, 'apples')
print('остаток ', k, 'apples')
