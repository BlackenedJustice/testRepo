def fact(n):
    fac=1
    for i in range(1,n+1,1):
        fac=fac*i
    return(fac)
print('enter the number')
n=int(input())
print(fact(n))
