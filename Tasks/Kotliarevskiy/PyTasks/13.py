print ('введите первое время')
h1, m1, s1 = (int(input()) for i in range(3))
print ('введите второе время')
h2, m2, s2 = (int(input()) for i in range(3))
d=3600*(h2-h1)+60*(m2-m1)+s2-s1
print(d,'секунд')
