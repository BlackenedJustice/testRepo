a = int(input())
b = int(input())

for i in range(a - (a+1) % 2, b + (b+1)%2 -1, -2):
    if i%2 == 1:
        print(i, end = ' ')
