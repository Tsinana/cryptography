import math
from utils.simpleOparections import powm


def isSimpleSquareRoot(n):
  for a in range(2, n - 1):
    if powm(a, 2, n) in {n - 1, 1}:
      return False
    
  return True


def isSimpleFerma(n):
  return powm(2, n - 1, n) == 1

def isSimpleMillerRabin(n):
  """Проверка на простоту с помощью теста Миллера-Рабина. Аргументы: n - проверяемое число, r - число проверок"""

  if n % 2 == 0:
    return False

  nMinesOne = n - 1
  r = round(math.log2(n))

  s = 0 # n - 1 = 2^s * d
  d = nMinesOne
  while d % 2 == 0:
    s += 1
    d /= 2

  for a in range(2, r + 1):
      x_0 = powm(a, d, n)

      if not(x_0 in {1, nMinesOne}):
        x_i = x_0
        nMinesOneInX = False

        for _ in range(s - 1):
          x_next = powm(x_i, 2, n)

          if x_next == nMinesOne:
            nMinesOneInX = True
            break

          x_i = x_next
        
        if not(nMinesOneInX):
          return False
        
  return True
