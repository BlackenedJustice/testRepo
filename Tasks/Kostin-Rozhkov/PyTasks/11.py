v, t = map(int, input().split())
print("Через {} часов Вася окажется на {} километре".format(t, v * t % 109))
