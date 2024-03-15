from utils.eulerFunction import eulerFunction


def multP(polynomialA, polynomialB, mod = -1, ):
  """Умножение двух полиномов. Умножение двух полиномов по модулю"""

  iterator = 0
  polynomialLastStep = 0

  modLength = -1
  if mod != -1:
    modClone = mod
    while modClone != 0:
      modLength += 1
      modClone >>= 1

  while 1 << iterator <= polynomialB:
    if polynomialB & 1 << iterator != 0:
      polynomialLastStep = polynomialLastStep ^ polynomialA << iterator

      if mod != -1 and polynomialLastStep >= 1 << modLength:
        polynomialLastStep = divP(polynomialLastStep, mod)[0]

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


def powP(polynomial, degree, mod = -1):
  """Возводит полином в степень. Возводит полином в степень по модулю"""

  polynomialAns = polynomial

  for step in range(degree - 1):
    polynomialAns = multP(polynomialAns, polynomial, mod)

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

      for divMO in divisorspMinusOne:
        if powP(startP,int(pMinusOne/divMO),simpleP) == 1:
          print(f"{bin(startP)} - не примитив, так как в степени {divMO} по модулю {bin(simpleP)} имеет остаток 1")

          isPrimitiveEl = False
          break

      if isPrimitiveEl:
        primitiveEs.append(startP)

      startP += 1

    ansArray.append([simpleP,primitiveEs]) 

  return ansArray



print(multP(0b1000000000000,0b1000,0b11001))
print(powP(0b1000,5,0b11001))