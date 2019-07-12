print ('введите cкорость и время')
v,t = (int(input()) for i in range(2))
v=(v*t)%109

if v<0:
    v=109+v

print(v)
