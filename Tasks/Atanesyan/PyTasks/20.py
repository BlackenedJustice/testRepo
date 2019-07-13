n = int(input())
i = 1
if n >= 10 or n < 1:
    print('error')
else:
    for i in range(n + 1):
        for j in range (i):
            print(j + 1, end='')
            j = j + 1
        print('')
