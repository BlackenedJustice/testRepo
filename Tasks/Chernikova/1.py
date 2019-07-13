Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> f1=f2=1
n= int(input())
i=0
while i < n-2:
    fsum = f1+f2
    f1= f2
    f2= fsum
    i += 1
print(f2)
