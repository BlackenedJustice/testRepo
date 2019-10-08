Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n
print(fact(5))
