def fact(n):
  k = 1
  for i in range(n):
      k *= i + 1
  return k

print("n! = {}".format(fact(int(input("Введите n: ")))))
