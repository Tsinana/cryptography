from utils.GFTwoWorkers import allPrimitiveElements, getInfoGFN
from utils.eulerFunction import *
from utils.simpleNumberTests import isSimpleMillerRabin, isSimpleSquareRoot

1
def main():
  print("\n\n\nПривет!\t(´・ω ・`）")

  while True:
    try:
        print("\n\nПрограммы:")
        print("(1)\tНахождение числа Эйлера")
        print("(2)\tВычисления целых степеней по заданному модулю ")
        print("(3)\tПостроения всех примитивов заданного поля GF(2^n)")
        print("(4)\tПостроение циклотомических классов с из мин полиномами")
        print("(5)\tПроверка на простоту числа")
        print("(0)\tВыход")

        choice = int(input("Выбор: "))
        print()
        if choice == 1:
          print("\nВыбор метода:")
          print("(1)\tМетод по формуле")
          print("(2)\tМетод по определению")
          print("(3)\tСравнение эффективности")
          method_choice = int(input("Выбор метода: "))
          ans_str = "Ответ: "
          if method_choice == 1:
            number = int(input("\nВведите число для нахождения функции Эйлера: "))
            ans_str += str(eulerFunctionAPriory(number))
          elif method_choice == 2:
            number = int(input("\nВведите число для нахождения функции Эйлера: "))
            ans_str += str(eulerFunction(number))
          elif method_choice == 3:
            ans_str += str(eulerFunctionsTest())
          else:
            ans_str = "Неверный выбор метода."
          print("\n" + ans_str)
        elif choice == 2:
          print("Для c ≡ a^b(mod n) введите соответствующие значения")
          a = int(input("a: "))
          b = int(input("b: "))
          n = int(input("n: "))
          print("\nc ≡ ", powm(a, b, n))
        elif choice == 3:
          print("Для поля GF(2^n) введите соответствующие значение")
          n = int(input("n: "))
          print()
          for arr in allPrimitiveElements(n):
            print("Неприводимый полином -",str(bin(arr[0])))
            print(list(map(lambda el: str(bin(el)), arr[1])))
        elif choice == 4:
          print("Для поля GF(2^n) введите соответствующие значение n и образующий многочлен")
          n = int(input("n: "))
          obr = int(input("Oбразующий многочлен: "))
          print(getInfoGFN(n, obr))
        elif choice == 5:
          print("\nВыбор теста:")
          print("(1)\tПроверка квадратичным корнем")
          print("(2)\tПроверка тестом Миллера-Рабина")
          method_choice = int(input("Выбор метода: "))
          print("\nВведите проверяемое число (n)")
          n = int(input("n: "))
          ans_str = "Ответ: "
          if method_choice == 1:
            ans_str += str(isSimpleSquareRoot(n))
          elif method_choice == 2:
            ans_str += str(isSimpleMillerRabin(n))
          else:
            ans_str = "Неверный выбор метода."
          print("\n" + ans_str)

        elif choice == 0:
           break
        else:
            print("Неверный выбор программы.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

  print("\n\nКак же ты был хорош сегодня! Заходи потом еще как-нибудь")
  print("／ﾌﾌ 　　　　　 　　 　ム｀ヽ\n/ ノ)　　 ∧　　∧　　　　）　ヽ\n/ ｜　　(´・ω ・`）ノ⌒（ゝ._,ノ\n/　ﾉ⌒＿⌒ゝーく　 ＼　　／\n丶＿ ノ 　　 ノ､　　|　/\n　　 `ヽ `ー-‘人`ーﾉ /\n　　　 丶 ￣ _人’彡ﾉ\n　　　／｀ヽ _/\\__'")
  

 
if __name__ == "__main__":
  main()

  