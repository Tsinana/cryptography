from utils.eulerFunction import *


def main():
  print("\n\n\nПривет!\t(´・ω ・`）")

  while True:
    try:
        print("\n\nПрограммы:")
        print("(1)\tНахождение числа Эйлера")
        print("(2)\tВычисления целых степеней по заданному модулю ")
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
        elif choice == 0:
           break
        else:
            print("Неверный выбор программы.")
    except ValueError:
        print("Пожалуйста, введите число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

  print("\n\nКак же ты был хорош сегодня! Заходи потом еще как-нибудь")
  print("／ﾌﾌ 　　　　　 　　 　ム｀ヽ\n/ ノ)　　 ∧　　∧　　　　）　ヽ\n/ ｜　　(´・ω ・`）ノ⌒（ゝ._,ノ\n/　ﾉ⌒＿⌒ゝーく　 ＼　　／\n丶＿ ノ 　　 ノ､　　|　/\n　　 `ヽ `ー-‘人`ーﾉ /\n　　　 丶 ￣ _人’彡ﾉ\n　　　／｀ヽ _/\\__'")
  

 
if __name__ == "__main__":
  main()

  