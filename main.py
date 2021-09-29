'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n == 1:
      return False
  elif n == 2:
    return True;
  else:
    for x in range(2, n):
      if n % x == 0:
        return False
    return True

  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  result = 1
  for x in lst:
    result = result * x
  return result
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if y == 0:
    return x
  else:
    return get_cmmdc_v1(y, (x % y))
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  r = x % y
  while r != 0:
    x = y
    y = r
    r = x % y
  return y
  
def main():
  myResult = is_prime(11)
  print(myResult)
  Cmmdc_one = get_cmmdc_v1(2, 12)
  print(Cmmdc_one)
  Cmmdc_two = get_cmmdc_v2(3, 18)
  print(Cmmdc_two)

if __name__ == '__main__':
  main()
