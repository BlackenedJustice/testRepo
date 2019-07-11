def sum_fact(n):
    sum = 0
    mult = 1
    for i in range(1,n+1):
        mult *= i
        sum += mult
    return sum
  