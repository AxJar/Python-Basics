"""
Axel Jarquin Morga // A01636324
Proyecto integrador
"""
import random


def sumas_p():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ｐｒｉｎｃｉｐｉａｎｔｅ ｄｅ ｓｕｍａｓ (➕ )\
          \n\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        suma = num1 + num2
        a.append(suma)
        result = int(input(f"\n{num1}  ➕  {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(1, 10)
            num4 = random.randint(10, 60)
            suma2 = num3 + num4
            a.append(suma2)
            result = int(input(f"\n{num3} ➕  {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara avanzar de categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def sumas_i():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ｉｎｔｅｒｍｅｄｉｏ ｄｅ ｓｕｍａｓ (➕ )\
          \n\t\t  Son 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        suma = num1 + num2
        a.append(suma)
        result = int(input(f"\n{num1}  ➕  {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 !  𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓲𝓷𝓽𝓮𝓻𝓶𝓮𝓭𝓲𝓸 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(10, 150)
            num4 = random.randint(10, 150)
            suma2 = num3 + num4
            a.append(suma2)
            result = int(input(f"\n{num3}  ➕  {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓲𝓷𝓽𝓮𝓻𝓶𝓮𝓭𝓲𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara avanzar de categoría necesitas al menos 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def sumas_a():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ａｖａｎｚａｄｏ ｄｅ ｓｕｍａｓ (➕ )\
          \n\t\t  Son 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(100, 500)
        num2 = random.randint(100, 500)
        suma = num1 + num2
        a.append(suma)
        result = int(input(f"\n{num1}  ➕  {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 👍👌")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(100, 1000)
            num4 = random.randint(100, 1000)
            suma2 = num3 + num4
            a.append(suma2)
            result = int(input(f"\n{num3}  ➕  {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara completar la categoría necesitas al menos 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊 ")
    crear_archivo(m)


def restas_p():
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
        result = int(input(f"\n{num1}  ➖  {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(10, 60)
            num4 = random.randint(1, 40)
            resta2 = num3 - num4
            a.append(resta2)
            result = int(input(f"\n{num3}  ➖  {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara avanzar de categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def restas_i():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ｉｎｔｅｒｍｅｄｉｏ ｄｅ ｒｅｓｔａｓ (➖ )\
            \n\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(10, 100)
        num2 = random.randint(1, 80)
        resta = num1 - num2
        a.append(resta)
        result = int(input(f"\n{num1}  ➖  {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓲𝓷𝓽𝓮𝓻𝓶𝓮𝓭𝓲𝓸 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(10, 150)
            num4 = random.randint(1, 100)
            resta2 = num3 - num4
            a.append(resta2)
            result = int(input(f"\n{num3}  ➖  {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓲𝓷𝓽𝓮𝓻𝓶𝓮𝓭𝓲𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara avanzar de categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def restas_a():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ａｖａｎｚａｄｏ ｄｅ ｒｅｓｔａｓ (➖ )\
            \n\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(100, 500)
        num2 = random.randint(10, 400)
        resta = num1 - num2
        a.append(resta)
        result = int(input(f"\n{num1}  ➖  {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(100, 1000)
            num4 = random.randint(10, 700)
            resta2 = num3 - num4
            a.append(resta2)
            result = int(input(f"\n{num3}  ➖  {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara completar la categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def multi_p():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ｐｒｉｎｃｉｐｉａｎｔｅ ｄｅ ｍｕｌｔｉｐｌｉｃａｃｉｏｎｅｓ (✖️  )\
            \n\t\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        multi = num1 * num2
        a.append(multi)
        result = int(input(f"\n{num1}  ✖️   {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(1, 50)
            num4 = random.randint(1, 10)
            multi2 = num3 * num4
            a.append(multi2)
            result = int(input(f"\n{num3}  ✖️   {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara avanzar de categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def multi_a():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ａｖａｎｚａｄｏ ｄｅ ｍｕｌｔｉｐｌｉｃａｃｉｏｎｅｓ (✖️  )\
            \n\t\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
        multi = num1 * num2
        a.append(multi)
        result = int(input(f"\n{num1}   ✖️   {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(10, 250)
            num4 = random.randint(10, 100)
            multi2 = num3 * num4
            a.append(multi2)
            result = int(input(f"\n{num3}   ✖️   {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara completar la categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def divisiones_p():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ｐｒｉｎｃｉｐｉａｎｔｅ ｄｅ ｄｉｖｉｓｉｏｎｅｓ (➗ )\
            \n\t\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2\
                \n\t\t\t\t\tredondea a 2 decimales , si se requiere")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        while True:
            num1 = random.randint(1, 100)
            num2 = random.randint(2, 10)
            if (num1 % 2 == 0) and (num2 % 2 == 0):
                break
        div = round((num1 / num2), 2)
        a.append(div)
        result = float(input(f"\n{num1}   ➗   {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓹𝓻𝓲𝓷𝓬𝓲𝓹𝓲𝓪𝓷𝓽𝓮 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            while True:
                num3 = random.randint(1, 500)
                num4 = random.randint(2, 20)
                if (num3 % 2 == 0) and (num4 % 2 == 0):
                    break
            div2 = round((num3 / num4), 2)
            a.append(div2)
            result = float(input(f"\n{num3}   ➗   {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara avanzar de categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def divisiones_a():
    print("\n\t\tＥｌｅｇｉｓｔｅ ｅｌ ｎｉｖｅｌ ａｖａｎｚａｄｏ ｄｅ ｄｉｖｉｓｉｏｎｅｓ (➗ )\
        \n\t\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2\
            \n\t\t\t\t\tredondea a 2 decimales , si se requiere")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        while True:
            num1 = random.randint(1, 500)
            num2 = random.randint(2, 20)
            if (num1 % 2 == 0) and (num2 % 2 == 0):
                break
        div = round((num1 / num2), 2)
        a.append(div)
        result = float(input(f"\n{num1}   ➗   {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            while True:
                num3 = random.randint(100, 1000)
                num4 = random.randint(1, 100)
                if (num3 % 2 == 0) and (num4 % 2 == 0):
                    break
            div2 = round((num3 / num4), 2)
            a.append(div2)
            result = float(input(f"\n{num3}   ➗   {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara completar la categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def potencias():
    print("\n\t\t\t\t\tＥｌｅｇｉｓｔｅ  ｐｏｔｅｎｃｉａｓ ( ^ )\
        \n\t\t\tSon 10 ejercicios diferentes // Completa al menos 7 para subir al nivel 2")
    aciertos = 0
    a = []
    r = []
    for i in range(10):
        num1 = random.randint(1, 5)
        num2 = random.randint(2, 3)
        pot = num1 ** num2
        a.append(pot)
        result = float(input(f"\n{num1}  ^  {num2} = "))
        r.append(result)
        if a[i] == r[i]:
            aciertos = aciertos + 1
            print("✔")
        else:
            print("✘")
    m.append(r)
    if aciertos >= 7:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\t¡ 𝓑𝓲𝓮𝓷 𝓱𝓮𝓬𝓱𝓸 ! 𝓼𝓾𝓫𝓮𝓼 𝓪𝓵 𝓷𝓲𝓿𝓮𝓵 2 𝓭𝓮 𝓹𝓸𝓽𝓮𝓷𝓬𝓲𝓪𝓼 👍👌 ")
        aciertos2 = 0
        a = []
        r = []
        for i in range(10):
            num3 = random.randint(1, 9)
            num4 = random.randint(2, 5)
            pot2 = num3 ** num4
            a.append(pot2)
            result = float(input(f"\n{num3}  ^  {num4} = "))
            r.append(result)
            if a[i] == r[i]:
                aciertos2 = aciertos2 + 1
                print("✔")
            else:
                print("✘")
        m.append(r)
        if aciertos2 >= 7:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 𝓵𝓪 𝓬𝓪𝓽𝓮𝓰𝓸𝓻𝓲́𝓪 𝓭𝓮 𝓪𝓿𝓪𝓷𝔃𝓪𝓭𝓸 😎👑")
        else:
            print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos2} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
            print("\n\tPara completar la categoría necesitas 7 aciertos, sigue practicando 😉👊")
    else:
        print(f"\n\t𝓗𝓪𝓼 𝓬𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓸 {aciertos} de 10 𝓬𝓸𝓻𝓻𝓮𝓬𝓽𝓪𝓶𝓮𝓷𝓽𝓮")
        print("\n\tPara avanzar de nivel necesitas al menos 7 aciertos, sigue practicando 😉👊")
    crear_archivo(m)


def inicio_menu():
    print("░░░░ ██╗██╗░░░██╗███████╗░██████╗░░█████╗░  ██████╗░███████╗\
        \n░░░░░██║██║░░░██║██╔════╝██╔════╝░██╔══██╗  ██╔══██╗██╔════\
        \n░░░░░██║██║░░░██║█████╗░░██║░░██╗░██║░░██║  ██║░░██║█████╗░░\
        \n██╗░░██║██║░░░██║██╔══╝░░██║░░╚██╗██║░░██║  ██║░░██║██╔══╝░░\
        \n╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚█████╔╝  ██████╔╝███████╗\
        \n░╚════╝░░╚═════╝░╚══════╝░╚═════╝░░╚════╝░  ╚═════╝░╚══════╝\
        \n░█████╗░██████╗░██████╗░███████╗███╗░░██╗██████╗░██╗███████╗░█████╗░░░░░░██╗███████╗\
        \n██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║██╔══██╗██║╚════██║██╔══██╗░░░░░██║██╔════╝\
        \n███████║██████╔╝██████╔╝█████╗░░██╔██╗██║██║░░██║██║░░███╔═╝███████║░░░░░██║█████╗░░\
        \n██╔══██║██╔═══╝░██╔══██╗██╔══╝░░██║╚████║██║░░██║██║██╔══╝░░██╔══██║██╗░░██║██╔══╝░░\
        \n██║░░██║██║░░░░░██║░░██║███████╗██║░╚███║██████╔╝██║███████╗██║░░██║╚█████╔╝███████╗\
        \n╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝")

    nombre = input("""\n
    ¡ Bɪᴇɴᴠᴇɴɪᴅᴏ ᴀ ᴛᴜ ᴊᴜᴇɢᴏ ᴅᴇ ᴀᴘʀᴇɴᴅɪᴢᴀᴊᴇ ! , ᴅᴏɴᴅᴇ ᴘᴏᴅʀᴀ́s ᴘʀᴀᴄᴛɪᴄᴀʀ ᴛᴜs ʜᴀʙɪʟɪᴅᴀᴅᴇs ᴍᴀᴛᴇᴍᴀ́ᴛɪᴄᴀs ᴅᴇ ᴜɴᴀ ᴍᴀɴᴇʀᴀ ᴅɪᴠᴇʀᴛɪᴅᴀ, ¿ Cᴏᴍᴏ ᴛᴇ ʟʟᴀᴍᴀs ? """)

    print("""

    █░█ █▀█ █░░ ▄▀█   ░   █▀▀ █▄░█   █▀▀ █▀ ▀█▀ █▀▀   ░░█ █░█ █▀▀ █▀▀ █▀█   █▀█ █░█ █▀▀ █▀▄ █▀▀ █▀
    █▀█ █▄█ █▄▄ █▀█   █   ██▄ █░▀█   ██▄ ▄█ ░█░ ██▄   █▄█ █▄█ ██▄ █▄█ █▄█   █▀▀ █▄█ ██▄ █▄▀ ██▄ ▄█

    █▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █ █▀▀ ▄▀█ █▀█   █░░ █▀█ █▀   █▀ █ █▀▀ █░█ █ █▀▀ █▄░█ ▀█▀ █▀▀ █▀
    █▀▀ █▀▄ █▀█ █▄▄ ░█░ █ █▄▄ █▀█ █▀▄   █▄▄ █▄█ ▄█   ▄█ █ █▄█ █▄█ █ ██▄ █░▀█ ░█░ ██▄ ▄█

    ▄▀█ █▀█ ▄▀█ █▀█ ▀█▀ ▄▀█ █▀▄ █▀█ █▀
    █▀█ █▀▀ █▀█ █▀▄ ░█░ █▀█ █▄▀ █▄█ ▄█""")
    while True:
        print("""\n
    ████████████████████████████████████████████
    █▀░████████─▄▄▄▄█▄─██─▄█▄─▀█▀─▄██▀▄─██─▄▄▄▄█
    ██░██░░████▄▄▄▄─██─██─███─█▄█─███─▀─██▄▄▄▄─█
    ▀▄▄▄▀▄▄▀▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
    ████████████████████████████████████████████████
    █▀▄▄▀███████▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄─▄─██▀▄─██─▄▄▄▄█
    ██▀▄██░░█████─▄─▄██─▄█▀█▄▄▄▄─███─████─▀─██▄▄▄▄─█
    ▀▄▄▄▄▀▄▄▀▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀
    ████████████████████████████████████████████████████████████████████████████████████████████████████████
    █▄▄▄░█████▄─▀█▀─▄█▄─██─▄█▄─▄███─▄─▄─█▄─▄█▄─▄▄─█▄─▄███▄─▄█─▄▄▄─██▀▄─██─▄▄▄─█▄─▄█─▄▄─█▄─▀█▄─▄█▄─▄▄─█─▄▄▄▄█
    ██▄▄░█░░███─█▄█─███─██─███─██▀███─████─███─▄▄▄██─██▀██─██─███▀██─▀─██─███▀██─██─██─██─█▄▀─███─▄█▀█▄▄▄▄─█
    ▀▄▄▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    █████████████████████████████████████████████████████████████████
    █░█░██████▄─▄▄▀█▄─▄█▄─█─▄█▄─▄█─▄▄▄▄█▄─▄█─▄▄─█▄─▀█▄─▄█▄─▄▄─█─▄▄▄▄█
    █▄▄░██░░███─██─██─███▄▀▄███─██▄▄▄▄─██─██─██─██─█▄▀─███─▄█▀█▄▄▄▄─█
    ▀▀▄▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    █████████████████████████████████████████████████████████████████
    █░▄▄▄███████▄─▄▄─█─▄▄─█─▄─▄─█▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█▄─▄██▀▄─██─▄▄▄▄█
    █▄▄▄▒█░░█████─▄▄▄█─██─███─████─▄█▀██─█▄▀─██─███▀██─███─▀─██▄▄▄▄─█
    ▀▄▄▄▄▀▄▄▀▀▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
    ████████████████████████████████████████
    █░▄▄▄███████─▄▄▄▄██▀▄─██▄─▄███▄─▄█▄─▄▄▀█
    █░▄▄░█░░████▄▄▄▄─██─▀─███─██▀██─███─▄─▄█
    █▄▄▄▄▀▄▄▀▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀
    """)
        opcion = int(input("""
    █▀▀ █▀ █▀▀ █▀█ █▀▀ █▀▀   █░█ █▄░█ ▄▀█   █▀█ █▀█ █▀▀ █ █▀█ █▄░█   █▀▄ █▀▀ █░░   █▀▄▀█ █▀▀ █▄░█ █░█ ▀
    ██▄ ▄█ █▄▄ █▄█ █▄█ ██▄   █▄█ █░▀█ █▀█   █▄█ █▀▀ █▄▄ █ █▄█ █░▀█   █▄▀ ██▄ █▄▄   █░▀░█ ██▄ █░▀█ █▄█ ▄  """))
        if opcion == 1:
            while True:
                print("""\n
                １．Ｓｕｍａｓ ｐｒｉｎｃｉｐｉａｎｔｅｓ
                ２．Ｓｕｍａｓ ｉｎｔｅｒｍｅｄｉｏ
                ３．Ｓｕｍａｓ Ａｖａｎｚａｄｏ
                ４．Ｖｏｌｖｅｒ ａｌ ｍｅｎｕ ｐｒｉｎｃｉｐａｌ""")
                opc = int(input("\n\tEscoge una categoría: "))
                if opc == 1:
                    sumas_p()
                elif opc == 2:
                    sumas_i()
                elif opc == 3:
                    sumas_a()
                elif opc == 4:
                    break
                else:
                    print("\n\t\t❌ 𝑬𝑺𝑻𝑨 𝑶𝑷𝑪𝑰𝑶𝑵 𝑵𝑶 𝑬𝑺 𝑽𝑨𝑳𝑰𝑫𝑨, 𝑰𝑵𝑻𝑬𝑵𝑻𝑨 𝑫𝑬 𝑵𝑼𝑬𝑽𝑶 ❌ ")
        elif opcion == 2:
            while True:
                print("""\n
                    １．Ｒｅｓｔａｓ ｐｒｉｎｃｉｐｉａｎｔｅｓ
                    ２．Ｒｅｓｔａｓ ｉｎｔｅｒｍｅｄｉｏ
                    ３．Ｒｅｓｔａｓ Ａｖａｎｚａｄｏ
                    ４．Ｖｏｌｖｅｒ ａｌ ｍｅｎｕ ｐｒｉｎｃｉｐａｌ""")
                opc = int(input("\n\tEscoge una categoría: "))
                if opc == 1:
                    restas_p()
                elif opc == 2:
                    restas_i()
                elif opc == 3:
                    restas_a()
                elif opc == 4:
                    break
                else:
                    print("\n\t\t❌ 𝑬𝑺𝑻𝑨 𝑶𝑷𝑪𝑰𝑶𝑵 𝑵𝑶 𝑬𝑺 𝑽𝑨𝑳𝑰𝑫𝑨, 𝑰𝑵𝑻𝑬𝑵𝑻𝑨 𝑫𝑬 𝑵𝑼𝑬𝑽𝑶 ❌ ")
        elif opcion == 3:
            while True:
                print("""\n
                    １．Ｍｕｌｔｉｐｌｉｃａｃｉｏｎｅｓ ｐｒｉｎｃｉｐｉａｎｔｅ
                    ２. Ｍｕｌｔｉｐｌｉｃａｃｉｏｎｅｓ Ａｖａｎｚａｄｏ
                    ３．Ｖｏｌｖｅｒ ａｌ ｍｅｎｕ ｐｒｉｎｃｉｐａｌ""")
                opc = int(input("\n\tEscoge una categoría: "))
                if opc == 1:
                    multi_p()
                elif opc == 2:
                    multi_a()
                elif opc == 3:
                    break
                else:
                    print("\n\t\t❌ 𝑬𝑺𝑻𝑨 𝑶𝑷𝑪𝑰𝑶𝑵 𝑵𝑶 𝑬𝑺 𝑽𝑨𝑳𝑰𝑫𝑨, 𝑰𝑵𝑻𝑬𝑵𝑻𝑨 𝑫𝑬 𝑵𝑼𝑬𝑽𝑶 ❌ ")
        elif opcion == 4:
            while True:
                print("""\n
                    １．Ｄｉｖｉｓｉｏｎｅｓ ｐｒｉｎｃｉｐｉａｎｔｅ
                    ２．Ｄｉｖｉｓｉｏｎｅｓ ａｖａｎｚａｄo
                    ３．Ｖｏｌｖｅｒ ａｌ ｍｅｎｕ ｐｒｉｎｃｉｐａｌ""")
                opc = int(input("\n\tEscoge una categoría: "))
                if opc == 1:
                    divisiones_p()
                elif opc == 2:
                    divisiones_a()
                elif opc == 3:
                    break
                else:
                    print("\n\t\t❌ 𝑬𝑺𝑻𝑨 𝑶𝑷𝑪𝑰𝑶𝑵 𝑵𝑶 𝑬𝑺 𝑽𝑨𝑳𝑰𝑫𝑨, 𝑰𝑵𝑻𝑬𝑵𝑻𝑨 𝑫𝑬 𝑵𝑼𝑬𝑽𝑶 ❌ ")
        elif opcion == 5:
            while True:
                print("""\n
                    １． Ｐｏｔｅｎｃｉａｓ
                    ２． Ｖｏｌｖｅｒ ａｌ ｍｅｎｕ ｐｒｉｎｃｉｐａｌ""")
                opc = int(input("\n\tEscoge una categoría: "))
                if opc == 1:
                    potencias()
                elif opc == 2:
                    break
                else:
                    print("\n\t\t❌ 𝑬𝑺𝑻𝑨 𝑶𝑷𝑪𝑰𝑶𝑵 𝑵𝑶 𝑬𝑺 𝑽𝑨𝑳𝑰𝑫𝑨, 𝑰𝑵𝑻𝑬𝑵𝑻𝑨 𝑫𝑬 𝑵𝑼𝑬𝑽𝑶 ❌ ")
        elif opcion == 6:
            print(f"""\n\t¡ Ｑｕｅ ｍａｌ ｑｕｅ ｔｅ ｖａｙａｓ {nombre} 😕 ！  ｅｓｐｅｒａｍｏｓ ｑｕｅ ｔｅ ｈａｙａｓ ｄｉｖｅｒｔｉｄｏ 😁
                ｒｅｃｕｅｒｄａ ｑｕｅ ｌａ ｐｒａｃｔｉｃａ ｈａｃｅ ａｌ ｍａｅｓｔｒｏ ✍ 😎👍 """)
            break
        else:
            print("\n\t\t❌ 𝑬𝑺𝑻𝑨 𝑶𝑷𝑪𝑰𝑶𝑵 𝑵𝑶 𝑬𝑺 𝑽𝑨𝑳𝑰𝑫𝑨, 𝑰𝑵𝑻𝑬𝑵𝑻𝑨 𝑫𝑬 𝑵𝑼𝑬𝑽𝑶 ❌ ")


def crear_archivo(mat):
    with open("../Manejo_archivos_python/Respuestas_juego.csv", "w") as outputFile:
        header = ""
        for i in range(len(mat)):
            header = header + ", " + "Respuesta parte" + str(i + 1) + "\n"
        header += "\n"
        outputFile.write(header)
        fila = ""
        for res in range(len(mat)):
            fila = fila + ", " + str(mat[res]) + "\n"
        outputFile.write(fila)


# Programa principal
m = []


def main():
    inicio_menu()


main()
