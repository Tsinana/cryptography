from math import sqrt
import random
from utils.simpleOparections import *
import time


def eulerFunctionAPriory(digit):
  """Функция Эйлера по определению"""

  counter = 1
  for i in range(2,digit):
    if isCoprime(digit, i):
      counter+=1

  return counter


def eulerFunction(dividend, getArr = False):
  """Функция Эйлера по формуле"""

  if not(isinstance(dividend, int)): 
    raise ValueError("Аргументом должно быть натуральное число")

  divisor = 2
  answer = dividend
  arrayDivisors = []
  
  while True:
    if divisor > dividend/2:
      break

    if dividend % divisor == 0:
      while dividend % divisor == 0:
        dividend = dividend / divisor
        arrayDivisors.append(divisor)

      answer *= 1 - 1/divisor

    divisor += 1

  if dividend != 1:
    answer *= 1 - 1/dividend
    arrayDivisors.append(dividend)

  if getArr:
    return round(answer), list(map(lambda x: round(x), arrayDivisors))

  return round(answer)


def eulerFunctionsTest():
  """Функция сравнения двух реализаций функции Эйлера"""

  oparetionCount = 0
  ans_str=""
  first_task = []
  second_task = []

  random_numbers = []
  for i in range(100): 
    random_numbers.append(random(10000000,10000100))

  start_time = time.time() 

  for number in random_numbers:
    oparetionCount+=1
    print(oparetionCount)
    first_task.append(eulerFunctionAPriory(number))

  end_time = time.time() 

  elapsed_time0 = end_time - start_time
  ans_str += (f'Затраченное время : {elapsed_time0} секунд. Алгоритм по описанию\n')

  start_time = time.time() 

  for number in random_numbers: 
    oparetionCount+=1
    print(oparetionCount)
    if eulerFunction(number) == 0:
      print (number)
    second_task.append(eulerFunction(number))

  end_time = time.time() 

  elapsed_time1 = end_time - start_time
  ans_str+=(f'Затраченное время : {elapsed_time1} секунд. Алгоритм по формулеn\n')
  ans_str+=(f'Отношение первого и второго алгоритма составляет: {round(elapsed_time0/elapsed_time1*100)}% \n')
  ans_str+=(f'Схожи ли решения задач двух алгоритмов {first_task==second_task}')

  return ans_str