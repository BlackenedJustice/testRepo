def fact(n):
  k = x = 1
  for i in range(n):
      k *= x
      x += 1
  return k

print("n! = {}".format(fact(int(input("Введите n: ")))))
