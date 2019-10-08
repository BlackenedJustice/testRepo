Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> n1, m1, n2, m2 = map(int, input('n1, m1, n2, m2')).split())
if (n1+m1+n2+m2)%2 == 0:
    print('YES')
else:
    print('NO')
