def num_ran():

    intentos = 8
    aleatorio = random.randint(1, 100)
    print("\nPromoción especial!, si adivinas un número entre 1 y 100 , te ganas una lavada gratis en tu próxima visita, tienes 8 intentos.")
    numero = int(input("Ingresa un numero de 1 a 100: "))
    while intentos > 1:
        if numero != aleatorio:
            intentos -= 1
            if numero > aleatorio:
                print("\nEl numero es mas chico. Tienes ", intentos, " intento(s) mas.\n")
            elif numero < aleatorio:
                print("\nEl numero es mas grande. Tienes ", intentos, " intento(s) mas.\n")
            numero = int(input("Ingresa un numero de 1 a 100: "))
        elif numero == aleatorio:
            print("\nFelicidades. Te haz ganado una lavada gratis en tu próxima visita.\n")
            break;
    if numero != aleatorio:
        print("\nPor poco, no pasa nada!. Suerte para la próxima!\n")

import random

def main():
    ganancias = 0
    while True:
        menu = int(input("\nMenu:\n1. Servicio de Lavado (incluye estacionamiento)\n2. Estacionamiento\n3. Juego en línea\n4. Salir\n"))
        if menu == 1:
            while True:
                lavado = int(input("\nElige una categoría de lavado:\n1. Automovil:\t$70.00\n2. Camioneta:\t$100.00\n"))
                if lavado == 1:
                    ganancias += 70
                    break
                elif lavado == 2:
                    ganancias += 100
                    break
                else:
                    print("\nEsta categoría no es valida, Ingresa de nuevo.")
            print("\nMuchas Gracias por su preferencia, te recuerdo que no te debes de preocupar por tu estacionamiento! regresa pronto!\n")
        elif menu == 2:
            while True:
                minutos = int(input("\n La Tarifa es de:$15.00/hr\nIngresa en minutos el tiempo que tu vehículo estuvo estacionado: "))
                if minutos > 0:
                    horas = minutos // 60
                    res_horas = minutos % 60
                    if res_horas != 0:
                        ganancias += (horas*15)+15
                        print("\n", horas, " horas de 60 minutos = $", horas*15, " pesos + ", res_horas, " minutos restantes = $ 15 pesos  *** Total a pagar $", (horas*15)+15, "***")
                    elif res_horas == 0:
                        ganancias += (horas*15)
                        print("\n", horas, " horas de 60 minutos = $", horas*15, " pesos + ", res_horas, " minutos restantes = $ 0 pesos  *** Total a pagar $", (horas*15), "***")
                    break
                else:
                    print("\nOpción no valida. Intentalo de nuevo.")
        elif menu == 3:
            num_ran()
        elif menu == 4:
            print("\nGanancias del dia: $", ganancias, "\nGracias por su preferencia.")
            break
        else:
            print("\nEsta opción no es valida, intenta de nuevo.")
main()