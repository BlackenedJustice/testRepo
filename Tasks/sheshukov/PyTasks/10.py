n, m, k = map(int, input().split())
if k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")