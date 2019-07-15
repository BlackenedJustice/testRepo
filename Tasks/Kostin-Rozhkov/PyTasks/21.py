print("Введите число карточек n: ")
n = int(input())
print("Введите карточки: ")
k = 0
for i in range(n - 1):
    k += int(input())
r = 0
for i in range(n):
    r += i + 1
print("Номер потерянной карточки равен {}".format(r - k))