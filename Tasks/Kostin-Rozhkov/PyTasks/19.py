def sum_fact(n):
  k = 1
  r = 0
  for i in range(n):
      k *= i + 1
      r += k
  return r

print("Сумма всех факториалов до n равна {}".format(sum_fact(int(input("Введите n: ")))))
