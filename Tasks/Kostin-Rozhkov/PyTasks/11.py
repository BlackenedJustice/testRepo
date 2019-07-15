print("Введите скорость v и время t: ")
v, t = map(int, input().split())
print("Через {} часов Вася окажется на {} километре".format(t, v * t % 109))
