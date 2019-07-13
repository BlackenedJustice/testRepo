Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum_fact(n):
res = 1
sumf = 0
for i in range(1, n + 1):
 res *= i
 sumf += res
return sumf
