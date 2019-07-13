Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b,c = map(int, input('a,b,c')).split())
if a== b==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print(0)
