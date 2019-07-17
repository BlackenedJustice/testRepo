j1 = int(input()) # столбец
i1 = int(input()) # строка
j2 = int(input()) 
i2 = int(input())
if abs(j1-j2) == 2 and abs(i1-i2) == 1 or abs(j1-j2) == 1 and abs(i1-i2) == 2:
	print("YES")
else:
	print("NO")