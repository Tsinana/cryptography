import math

from simpleOparections import gcd, powm


def priFacFerma(n):
  x = round(math.sqrt(n)+0.5)
  while x < n:
    w = x * x - n
    if math.sqrt(w) % 1 == 0:
      y = round(math.sqrt(w))
      a = x + y
      b = x - y
      return a, b
    x += 1
  
  return None

def priFacPollard(n,b = 2):
  while b < 100:
    a = 2
    e = 2

    while e <= b:
      a = powm(a, e, n)
      e += 1

    p = math.gcd(a - 1, n)

    if 1 < p and p < n:
      return p, b
    
    b *= b
  
  return None

def f(x):
  return (x + 1) * (x + 1)

def priFacPoPollard(n, seed = 2):
  x = seed
  y = seed
  divisor = 1
  
  while divisor == 1 or divisor == n:
    y = f(y) % n
    x = f(f(x) % n) % n
    print(y, x)
    divisor = math.gcd(abs(x - y), n)
    print(divisor)
  
  return divisor
   

print(priFacPollard(57247159,10))