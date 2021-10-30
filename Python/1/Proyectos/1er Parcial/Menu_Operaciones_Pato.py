# Examen practico
# Patricio Baeza Rubin de celis  -  A00830421#

''' Programa destinado a niños para practicar su calculo mental'''
seguir = 'Si'

marcadorf = 0
marcadora = 0

import random

def sumas():
    marcador = 0
    print("Suma los siguientes numeros: ")
    for i in range(5):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        suma = num1+num2
        resultado = int(input(f"\n{num1}+{num2} = "))
        if resultado == suma:
            marcador += 1
        elif resultado != suma:
            marcador -= 1
    return marcador

def resta():
    marcador = 0
    print("Resta los siguientes numeros: ")
    for i in range(5):
        num3 = random.randint(1, 9)
        num4 = random.randint(1, 9)
        resta = num3-num4
        resultado = int(input(str(num3) +'-'+ str(num4) + ' = '))
        if resultado == resta:
            marcador = marcador +1
        elif resultado != resta:
            marcador = marcador - 1       
    return marcador

def multiplicacion():
    marcador = 0
    print("Multiplica los siguientes numeros: ")
    for i in range(5):
        num5 = random.randint(1, 9)
        num6 = random.randint(1, 9)
        multiplicacion = num5*num6
        resultado = int(input(str(num5) +'*'+ str(num6) + ' = '))
        if resultado == multiplicacion:
            marcador = marcador+1
        elif resultado != multiplicacion:
            marcador = marcador - 1
    return marcador


print('Hola! para empezar elige una opcion')
# PROGRAMA PRINCIPAL
menu = 0
while menu != 4:
    print('MENU DE FUNCIONES:')
    print('Para operaciones de Suma, precione 1')
    print('Para operaciones de Resta, precione 2')
    print('Para operaciones de Multiplicacion, precione 3')
    print('Para salir, precione 4')
    menu = int(input("Elija una opción del menú: "))

    if menu == 1: #suma de dos numeros
        marcadora = sumas()
        marcadorf += marcadora
    
    if menu == 2: #Resta de dos numeros
        marcadora = resta()
        marcadorf += marcadora
    
    if menu == 3: #Multplicacion de dos numeros
        marcadora = multiplicacion()
        marcadorf += marcadora
    
    elif menu == 4:
        print(marcadorf)
    