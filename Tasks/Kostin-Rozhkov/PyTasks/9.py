print("Введите координаты клетки коня и требуемой клетки: ")
a, b, c, d = map(int, input().split())

if abs((c - a) * (d - b)) == 2:
    print ("Конь может одним ходом попасть в требуемую клетку")
else:
    print ("Конь не может одним ходом попасть в требуемую клетку")
