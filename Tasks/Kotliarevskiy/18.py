def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    return fact
print('enter the number')
n=int(input())
print(fact(n))
