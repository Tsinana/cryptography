import math


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

print(priFacFerma(1219))