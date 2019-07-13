print('enter the numbers')
n, m, k = (int(input()) for i in range(3))
p=m*n
if ((k%n==0) and (k//n<m)) or ((k%m==0) and (k//m<n)):
    ans='yes'
else:
    ans='no'
print(ans)
