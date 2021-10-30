'''
Hecho por: Axel Jarquin Morga//A01636324
Examen Primer Parcial
Entradas:Numero de minutos
Salidas:Monto a pagar dependiendo de los minutos que haya estado estacionado
'''
from math import *
import random


def numero_random():

    intentos = 8
    aleatorio = random.randint(1, 100)
    print("Promoción especial!, si adivinas un número entre 1 y 100 , te ganas una lavada gratis en tu próxima visita, tienes 8 intentos.")
    numero = int(input("Ingresa u numero del 1 al 100: "))
    while intentos > 1:
        if numero != aleatorio:
            intentos -= 1
            if numero > aleatorio:
                print("El numero es mas chico. Tienes ",intentos, " intento(s) mas")
            elif numero < aleatorio:
                print("El numero es mas grande. Tienes ",intentos, " intento(s) mas")
            numero = int(input("Ingresa un numero de 1 a 100: "))
        elif numero == aleatorio:
            print("Felicidades. Te haz ganado una lavada gratis en tu próxima visita.")
            break
    if numero != aleatorio:
        print("Por poco, no pasa nada!. Suerte para la próxima!")


# PROGRAMA PRINCIPAL
def main():
    menu = 1
    ganancias = 0
    while menu != 4:
        print("MENU COBRO DE SERVICIOS: \n\t\t 1. Servicio de Lavado (incluye estacionamiento) \n\t\t 2. Estacionamiento \n\t\t 3. Juego en linea \n\t\t 4. Salir Servicio de Lavado")
        # Selección de opción.
        menu = int(input("Elige una opción del menú: "))
        if menu == 1:
            lavado = int(input("\nElige una categoría de lavado:\n1. Automovil:\t$70.00\n2. Camioneta:\t$100.00\n"))
            if lavado == 1:
                ganancias += 70
            elif lavado == 2:
                ganancias += 100
            else:
                print("\nEsta categoría no es valida, Ingresa de nuevo.")
            print("\nMuchas Gracias por su preferencia, te recuerdo que no te debes de preocupar por tu estacionamiento! regresa pronto!\n")
        elif menu == 2:
            minutos = int(input(
                "\n La Tarifa es de: $15.00/hr\nIngresa en minutos el tiempo que tu vehículo estuvo estacionado: "))
            if minutos > 0:
                horas = minutos // 60
                res_horas = minutos % 60
                if res_horas != 0:
                    ganancias += (horas*15)+15
                    print("\n", horas, " horas de 60 minutos = $", horas*15, " pesos + ", res_horas,
                          " minutos restantes = $ 15 pesos  *** Total a pagar $", (horas*15)+15, "***")
                elif res_horas == 0:
                    ganancias += (horas*15)
                    print("\n", horas, " horas de 60 minutos = $", horas*15, " pesos + ", res_horas,
                          " minutos restantes = $ 0 pesos  *** Total a pagar $", (horas*15), "***")
            else:
                print("\nOpción no valida. Intentalo de nuevo.")
        elif menu == 3:
            numero_random()
        elif menu == 4:
            print("\nGanancias del dia: $", ganancias,"\nGracias por su preferencia.")
            break
        else:
            print("\nEsta opción no es valida, intenta de nuevo.")
main()
