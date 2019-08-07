def sum_fact(n):
    s=1
    fac=1
    if n>1:
        for i in range (2,n+1):
            fac=fac*i
            s=s+fac
    return s
print('enter the number')
n=int(input())
print(sum_fact(n))
    
