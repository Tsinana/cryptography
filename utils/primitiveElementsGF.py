from utils.eulerFunction import eulerFunction


def multP(polynomialA, polynomialB):
  """Умножение двух полиномов"""

  iterator = 0
  polynomialLastStep = 0

  while 1 << iterator <= polynomialB:
    if polynomialB & 1 << iterator != 0:
      polynomialLastStep = polynomialLastStep ^ polynomialA << iterator

    iterator += 1

  return polynomialLastStep


def divP(polynomial, divider):
  """Деление полинома с остатком. Возвращает частное и остаток"""

  if divider == 0:
    raise ValueError("Делитель равен нулю")

  iterator = 1
  quotient = 0b0

  dividerLength = -1
  dividerClone = divider

  while dividerClone != 0:
    dividerLength += 1
    dividerClone >>= 1

  while 1 << (iterator + dividerLength) <= polynomial:
    iterator += 1  
  iterator -= 1

  while polynomial >= 1 << dividerLength:
   
    while 1 << (iterator + dividerLength) > polynomial:
      iterator -= 1

    polynomial ^= divider << iterator
    quotient += 1 << iterator

  return (polynomial, quotient)
    

def isSimple(polynomial):
  """Проверяет полином на простоту"""

  divisor = polynomial - 1 

  while divisor != 1:

    if divP(polynomial, divisor)[0] == 0:
      return False
    
    divisor -= 1

  return True


def allSimplePolynomials(n):
  """Возвращает все простые полиномы заданной степени"""

  startP = 1 << n
  endP = 1 << (n + 1)
  simplePs = []

  while startP < endP:

    if isSimple(startP):
      simplePs.append(startP)

    startP += 1

  return simplePs


def povP(polynomial, degree):
  """Возводит полином в степень"""

  polynomialAns = polynomial

  for step in range(degree):
    polynomialAns = multP(polynomialAns, polynomial)

  return polynomialAns


def allPrimitiveElements(n):
  """Возвращает все примитивы поля по заданной степени двойки"""

  simplePs = allSimplePolynomials(n)
  pMinusOne = pow(2, n) - 1
  _, divisorspMinusOne = eulerFunction(pMinusOne, True)
  ansArray = [] 

  for simpleP in simplePs:

    startP = 0b10
    endP = 1 << n
    primitiveEs = []

    while startP < endP:
      isPrimitiveEl = True

      for divMO in range(1,pMinusOne-1):
        if divP(povP(startP,int(divMO)),simpleP)[0] == 1:
          print(f"{bin(startP)} - не примитив, так как в степени {divMO} по модулю {bin(simpleP)} имеет остаток 1")

          isPrimitiveEl = False
          break

      if isPrimitiveEl:
        primitiveEs.append(startP)

      startP += 1

    ansArray.append([simpleP,primitiveEs]) 

  return ansArray



print(divP(0b10001,0b10011))