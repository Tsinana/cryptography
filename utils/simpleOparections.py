def isCoprime(digit1, digit2):
  """Проверка на то, что два числа взаимо простые"""

  return gcd(digit1,digit2) == 1

def gcd(digit1, digit2):
  """НОД двух чисел """

  if not(isinstance(digit1, int) and isinstance(digit2, int)): 
    raise ValueError("Аргументом должны быть натуральные числа")
  
  dividend = digit1
  divisor = digit2
  if digit1 < digit2:
    dividend = digit2
    divisor = digit1

  while True:
    remainter = dividend % divisor
    if remainter == 0:
      break

    dividend = divisor
    divisor = remainter

  return divisor


def powm(a, b, n):
  c = 1
  while b:
    if b % 2 == 0:
      b /= 2
      a = (a * a) % n
    else:
      b -= 1
      c = (c * a) % n
  return c