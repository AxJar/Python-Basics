"""
made By:
Axel Jarquin Morga//A01636324

Aplicación para niños para practicar cálculo mental.
Sumas
Restas
Multiplicación


"""
import random
salon_fama = ""
# Función sumas
def sumas(name):
    print("Suma los siguientes números: ")
    aciertos = 0
    for i in range(5):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        suma = num1+num2
        resultado = int(input(f'{num1} + {num2} = '))
        if resultado == suma:
            aciertos = aciertos+1
    if aciertos == 5:
        print(f"¡Enhorabuena! {name} Tuviste 5 aciertos. Subes al nivel 2")
        aciertos2 = 0
        for i in range(5):
            num3 = random.randint(1, 9)
            num4 = random.randint(10, 100)
            suma2 = num3+num4
            resultado = int(input(f'{num3} + {num4} = '))
            if resultado == suma2:
                aciertos2 = aciertos2+1
        if aciertos2 == 5:
            print(f'¡Enhorabuena! {name} Todas tus respuestas fueron correctas. ¡Te ganaste un lugar en el salón de la fama!')
            salon_fama = name
        else:
            print("Tuviste un error, no pasa nada, repitelo de nuevo")
    else:
        print("Tuviste un error, no pasa nada, repitelo de nuevo")
# Funcion restas
def restas(name):
    restas_2(random.randint(10, 100), random.randint(10, 100))
    restas_2(random.randint(10, 100), random.randint(10, 100))
    restas_2(random.randint(10, 100), random.randint(10, 100))
    restas_2(random.randint(10, 100), random.randint(10, 100))
    restas_2(random.randint(10, 100), random.randint(10, 100))
    print(f'¡Felicidades! {name} contestaste todas las operaciones bien')
def restas_2(numero1, numero2):
    seguir = False
    while not seguir:
        n1 = int(input(f'Escribe el resultado de {numero1} - {numero2} = '))
        if n1 == numero1-numero2:
            seguir = True
        else:
            print("Resultado incorrecto, repitelo de nuevo")
# Función multiplicación
def multiplicacion(name):
    aciertos = 0
    errores = 0
    for i in range(10):
        acierto_error = multiplicacion_2(random.randint(1, 9), random.randint(1, 9))
        if acierto_error == 1:
            aciertos = aciertos+1
        else:
            errores = errores+1
    print(f'{name} , tuviste {aciertos} aciertos y {errores} errores')
def multiplicacion_2(numero1, numero2):
    acierto_error = 0
    resultado = int(input(f'Escribe el resultado de {numero1} * {numero2} = '))
    if resultado == numero1*numero2:
        acierto_error = 1
    else:
        print("Resultado incorrecto, ¡venga tu puedes!")
        acierto_error = -1
    return acierto_error

# PROGRAMA PRINCIPAL
salir = False
nombre = input("Dame tu nombre ")
while not salir:
    print("MENU DE FUNCIONES: \n\t 1. Sumas \n\t 2. Restas \n\t 3. Multiplicacion \n\t 4. SALIR")
    menu = int(input("Elija una opción del menú: "))

    if menu == 1: #suma de dos numeros
        sumas(nombre)
    if menu == 2: #Resta de dos numeros
        restas(nombre)
    if menu == 3: #Multplicacion de dos numeros
        multiplicacion(nombre)
    if menu == 4:#Salir
        salir = True
        print(f"{nombre} Gracias por usar este programa, no olvides practicar, ¡bonito dia!")