print("Введите размеры шоколадки n x m и требуемое число долек k: ")
n, m, k = map(int, input().split())

if k < n * m and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")