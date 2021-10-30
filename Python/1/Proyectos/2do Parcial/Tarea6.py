"""
María Fernanda Flores Salas		A01634543
Axel Jarquin Morga			    A01636324
Joel Isaias Solano Ocampo		A01639289
"""

import random

"""Función 1:
La función devuelve una lista que representa una matriz de nXn y cada localidad de la matriz tiene asignado el valor de -1."""
def crea_matriz1(n):
    m = []
    for a in range(n):
        m.append([])
        for b in range(n):
            m[a].append(-1)
    return m

"""Función 2:
La función devuelve una lista que representa una matriz de nXn y cada localidad de la matriz tiene asignado el número de su respectiva columna."""
def matriz_columna(n):
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(j)
    return m

"""Función 3:
La función devuelve una lista que representa una matriz de nXn y cada localidad de la matriz tiene asignado el valor de su correspondiente renglón."""
def matriz_renglon(n):
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(i)
    return m

"""Función 4:
La función devuelve una lista que representa una matriz de n1Xn2 y regresa una matriz a la cual se le asignaron números aleatorios entre 0 y 100."""
def matriz_aleatoria(n1, n2):
    m = []
    for a in range(n1):
        m.append([])
        for b in range(n2):
            ran = random.randint(0, 100)
            m[a].append(ran)
    return m

"""Función 5:
La función devuelve una lista que representa una matriz de nXn y cada localidad de la matriz tiene asignado un número consecutivo a partir de uno, por renglones."""
def matriz_secuencia(n):
    cont = 1
    matriz = []
    for i in range(n):
        lista = []
        for j in range(n):
            lista.append(cont)
            cont += 1
        matriz.append(lista)
    return matriz

"""Función 6:
La función devuelve una lista que representa una matriz de nXn y cada localidad de la matriz tiene asignado un número consecutivo a partir de uno, por columnas."""
def matriz_secuencia_columna(n):
    m = []
    count = 0
    for i in range(n):
        m.append([])
    for a in range(n):
        for b in range(n):
            m[b].append(count)
            count += 1
    return m

"""Función 7:
La función recibe como parámetro una lista anidada de números y regresa cuántos números pares hay dentro de la lista."""
def cuenta_pares(l):
    count = 0
    for a in range(len(l)):
        for b in l[a]:
            if b%2 == 0:
                count += 1
    return count

"""Función 8:
La función regresa el número de valores mayores o iguales que cero almacenados en la lista."""
def cuenta_positivos(l):
    count = 0
    for a in range(len(l)):
        for b in l[a]:
            if b >= 0:
                count += 1
    return count

"""Función 9:
La función modifica la lista, asignando el valor de 0 a cada localidad que contenga un valor menor a cero."""
def cambia_negativos(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] < 0:
                m[i][j] = 0
    return m

"""Función 10:
La función regresa el número de veces que se repite el valor de x en la lista."""
def cuenta_repeticiones(l, x):
    count = 0
    for i in range(len(l)):
        for num in l[i]:
            if num == x:
                count += 1
    return count

"""Función 11:
La función regresa el valor True si el valor de x existe en una localidad de la matriz y False si no existe."""
def busca(l, x):
    for i in range(len(l)):
        for num in l[i]:
            if num == x:
                return True
    return False

"""Función 12:
La función deberá devolver la suma de todos aquellos números que haya dentro de la matriz que sean mayores a 5."""
def suma_mayores5(l):
    add = 0
    for i in range(len(l)):
        for num in l[i]:
            if num > 5:
                add += num
    return add

"""Función 13:
La función deberá sustituir todos aquellos ceros que haya dentro de la matriz por el resultado de la suma de su número de renglón por su número de columna."""
def cambia_ceros(l):
    for a in range(len(l)):
        for b in range(len(l[a])):
            if l[a][b] == 0:
                l[a][b] = a+b
    return l

""" Programa principal """
print("\t\t¡Bienvenido! \nEn este programa podrás crear y manipular matrices con distintas opciones.")
while True:
    print("\n\t\t\t-Menu-")
    print("1. Crea Matriz \t\t\t8. Cuenta Positivos")
    print("2. Matriz Columna \t\t9. Cambia Negativos")
    print("3. Matriz Renglón \t\t10. Cuenta Repeticiones")
    print("4. Matriz Aleatoria \t\t11. Busca")
    print("5. Matriz Secuencia \t\t12. Suma Mayores a 5")
    print("6. Matriz Secuencia Columna \t13. Cambia Ceros")
    print("7. Cuenta Pares \t\t14. Salir")
    opc = int(input("Elige una opción: "))
    print()
    if opc == 1:
        print("\t\t\tCrea Matriz")
        print("En esta función se crea una matriz de números -1 con la cantidad de renglones y columnas que indiques.")
        num = int(input("Ingresa un número que represente el número de renglones y columnas de tu matriz: "))
        print(*crea_matriz1(num), sep = "\n")
    elif opc == 2:
        print("\t\t\tMatriz Columna")
        print("En esta función se crea una matriz con la cantidad de renglones y columnas que indiques, \n con el conteo de los números de izquierda a derecha, cada columna con el mismo dato en cada posición.")
        num = int(input("Ingresa un número que represente el número de renglones y columnas de tu matriz: "))
        print(*matriz_columna(num), sep = "\n")
    elif opc == 3:
        print("\t\t\tMatriz Renglón")
        print("En esta función se crea una matriz con la cantidad de renglones y columnas que indiques, \n con el conteo de los números de arriba hacia abajo, cada renglón con el mismo dato en cada columna.")
        num = int(input("Ingresa un número que represente el número de renglones y columnas de tu matriz: "))
        print(*matriz_renglon(num), sep = "\n")
    elif opc == 4:
        print("\t\t\tMatriz Aleatoria")
        print("En esta función se crea una matriz de números aleatorios con la cantidad de renglones y columnas que indiques.")
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        print(*matriz_aleatoria(num1, num2), sep = "\n")
    elif opc == 5:
        print("\t\t\tMatriz Secuencia")
        print("En esta función se crea una matriz de números consecutivos de izquierda a darecha\n por renglón con la cantidad de renglones y columnas que indique.")
        num = int(input("Ingresa un número que represente el número de renglones y columnas de tu matriz: "))
        print(*matriz_secuencia(num), sep = "\n")
    elif opc == 6:
        print("\t\t\tMatriz Secuencia Columna")
        print("En esta función se crea una matriz de números consecutivos por columna de izquierda a darecha\n con la cantidad de renglones y columnas que indique.")
        num = int(input("Ingresa un número que represente el número de renglones y columnas de tu matriz: "))
        print(*matriz_secuencia_columna(num), sep = "\n")
    elif opc == 7:
        print("\t\t\tCuenta Pares")
        print("Esta función crea una matriz a partir de los números que ingrese con la cantidad de renglones y columnas que indique, \n se contará la cantidad de números pares en su matriz.")
        la = []
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        for a in range(num2):
            la.append([])
            print("Ingresa ", num1, " número(s) para tu lista ", a, " de tu matriz:")
            for b in range(num1):
                num = int(input())
                la[a].append(num)
        print("Números pares en la matriz: ", cuenta_pares(la))
    elif opc == 8:
        print("\t\t\tCuenta Positivos")
        print("Esta función crea una matriz a partir de los números que ingrese con la cantidad de renglones y columnas que indique, \n se contarán la cantidad de números positivos en su matriz.")
        la = []
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        for a in range(num2):
            la.append([])
            print("Ingresa ", num1, " número(s) para tu lista ", a, " de tu matriz:")
            for b in range(num1):
                num = int(input())
                la[a].append(num)
        print("Números positivos en la matriz: ", cuenta_positivos(la))
    elif opc == 9:
        print("\t\t\tCambia Negativos")
        print("Esta función crea una matriz a partir de los números que ingrese con la cantidad de renglones y columnas que indique, \n se cambiarán los números negativos en su matriz por un 0.")
        la = []
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        for a in range(num2):
            la.append([])
            print("Ingresa ", num1, " número(s) para tu lista ", a, " de tu matriz:")
            for b in range(num1):
                num = int(input())
                la[a].append(num)
        print(*cambia_negativos(la), sep = "\n")
    elif opc == 10:
        print("\t\t\tCuenta Repeticiones")
        print("Esta función crea una matriz a partir de los números que ingrese con la cantidad de renglones y columnas que indique, \n se contará la cantidad de veces que se repita en su matriz el número que desee verificar.")
        la = []
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        for a in range(num2):
            la.append([])
            print("Ingresa ", num1, " número(s) para tu lista ", a, " de tu matriz:")
            for b in range(num1):
                num = int(input())
                la[a].append(num)
        numx = int(input("Ingresa un número que represente el número a comparar en tu matriz: "))
        print("Número de veces que se repite ", numx, ": ", cuenta_repeticiones(la, numx))
    elif opc == 11:
        print("\t\t\tBusca")
        print("Esta función crea una matriz a partir de los números que  ingrese con la cantidad de renglones y columnas que indique, \n podrá verificar si existe algún valor dentro de su matriz con respuesta de True en caso de existir o de False en caso de no hacerlo")
        la = []
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        for a in range(num2):
            la.append([])
            print("Ingresa ", num1, " número(s) para tu lista ", a, " de tu matriz:")
            for b in range(num1):
                num = int(input())
                la[a].append(num)
        numx = int(input("Ingresa un número que represente el número a buscar en tu matriz: "))
        print("Número ", numx, " a buscar en la matriz: ", busca(la, numx), sep = "\n")
    elif opc == 12:
        print("\t\t\tSuma Mayores a 5")
        print("Esta función crea una matriz a partir de los números que ingrese con la cantidad\n de renglones y columnas que ingrese y suma todos los números en la matriz mayores a 5.")
        la = []
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        for a in range(num2):
            la.append([])
            print("Ingresa ", num1, " número(s) para tu lista ", a, " de tu matriz:")
            for b in range(num1):
                num = int(input())
                la[a].append(num)
        print("Suma de todos los números mayores a 5: ", suma_mayores5(la))
    elif opc == 13:
        print("\t\t\tCambia Ceros")
        print("Esta función crea una matriz a partir de los números que ingrese con la cantidad de columnas \n y renglones que indique y reemplaza todos los ceros en la matriz por el total de los números que ingresó")
        la = []
        num1 = int(input("Ingresa un número que represente el número de renglones de tu matriz: "))
        num2 = int(input("Ingresa un número que represente el número de columnas de tu matriz: "))
        for a in range(num2):
            la.append([])
            print("Ingresa ", num1, " número(s) para tu lista ", a, " de tu matriz:")
            for b in range(num1):
                num = int(input())
                la[a].append(num)
        print(*cambia_ceros(la), sep = "\n")
    elif opc == 14:
        print("Gracias por utilizar el programa.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")