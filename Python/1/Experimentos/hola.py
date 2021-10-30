print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ｐｒｉｎｃｉｐｉａｎｔｅ ｄｅ ｒｅｓｔａｓ (➖ )\
            \n\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
     aciertos = 0
     a = []
     r = []
     for i in range(10):
          num1 = random.randint(1, 15)
          num2 = random.randint(1, 9)
          resta = num1 - num2
          a.append(resta)
          result = int(input(f"\n{num1} ➖  {num2} = "))
          r.append(result)
          if a[i] == r[i]:
               aciertos = aciertos + 1
               print("✔")
          else:
               print("✘")
     if aciertos >= 7:
          print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 👍👌 ")
          aciertos2 = 0
          a = []
          r = []
          for i in range(10):
               num3 = random.randint(10, 60)
               num4 = random.randint(1, 40)
               resta2 = num3 - num4
               a.append(resta2)
               result = int(input(f"\n{num3} ➖  {num4} = "))
               r.append(result)
               if a[i] == r[i]:
                    aciertos2 = aciertos2 + 1
                    print("✔")
               else:
                    print("✘")
          if aciertos2 >= 7:
               print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 😎👑")
          else:
               print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
               print("\n\tPara avanzar de categoría necesitas 7 aciertos, sigue practicando 😉👊")
     else:
          print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
          print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")