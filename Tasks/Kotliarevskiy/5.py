print('enter a,b,l,N')
a, b, l, N = (int(input()) for i in range(4))
l=N*a*2+(N-1)*b+2*l
print('длина равнa',l)

