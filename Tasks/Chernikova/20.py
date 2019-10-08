Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j)
    print()
