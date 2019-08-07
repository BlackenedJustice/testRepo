def sgn(x):
    if x>0:
        sign='1'
    elif x<0:
        sign='-1'
    else:
        sign='0'
    print(sign)
    return sgn


print('enter the number')
x=int(input())
sgn(x)
