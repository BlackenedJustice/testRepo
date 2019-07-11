def sum_fact(n):
  k = x = 1
  r = 0
  for i in range(n):
      k *= x
      x += 1
      r += k
  return r

print("Сумма всех факториалов до n равна {}".format(sum_fact(int(input("Введите n: ")))))
