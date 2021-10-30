"""


Programa con 5 funciones.
"""

# Librería
from math import *

# Función segundos.
def segundos (s):
    dias = s // 86400 # Hay 86400 segundos en un día.
    residuo = s % 86400 #El residuo de la división para calcular las horas.
    horas = residuo // 3600 #Una hora tiene 3600 segundos.
    residuo = residuo % 3600 #Volvemos a reiterar el residuos para calcular los minutos.
    minutos = residuo // 60 #Cada minuto tiene 60 segundos.
    residuo = residuo % 60 #Lo que sobre equivale a los segundos.
    print (f"Esta cantidad de segundos equivale a: \n\t {dias} días \n\t {horas} horas \n\t {minutos} minutos \n\t {residuo} segundos")


# Función conversión de pies a centímetros.
def pies_a_cm (p):
    return p * 30.48 #Un pie equivale a 30.48 centímetros.


# Funcion volumen_esfera
def volumen_esfera(r):
    v = (4/3)*pi*r**3
    return v

# Función  múltiplo_de
def multiplo_de(n1, n2):
    if n1%n2 == 0:
        return True
    else:
        return False

# Funcion compara
def compara(n1, n2):
    if n1 < n2:
        return -1
    elif n1 == n2:
        return 0
    else:
        return 1

# PROGRAMA PRINCIPAL
print ("MENU DE FUNCIONES: \n\t 1. Segundos a Días, Horas, Minutos \n\t 2. Pies a Centímetros \n\t 3. Volumen Esfera \n\t 4. Múltiplos Numéricos \n\t 5. Compara\n\t 6. SALIR")

menu = int(input("Elige una opción del menú: ")) #Selección de opción.

if menu == 1: #Segundos a Días, Horas, Minutos
    segs = int(input("Indica la cantidad de segundos a convertir en días, horas y minutos: "))
    segundos(segs)

elif menu == 2: #Pies a Centímetros
    pies = float(input("Indica la cantidad de pies a convertir en centímetros: "))
    ftacm = pies_a_cm (pies)
    print (f"\n\t {pies} pies equivalen a \n\t {ftacm} centímetros")

elif menu == 3: #Volumen Esfera
    radio = float(input("Indica el radio en cm de la esfera "))
    volumen = volumen_esfera(radio)
    print(f"\n\t El volumen de la esfera es {volumen:.2f} cm^3")

elif menu == 4: #Multiplos Numericos
    num1 = int(input("Indica un numero: "))
    num2 = int(input("Indica otro numero: "))
    multiplo = multiplo_de(num1, num2)
    print(f"\n\t {multiplo}")

elif menu == 5: #Compara
    num1 = int(input("Indica un numero: "))
    num2 = int(input("Indica otro numero: "))
    comp = compara (num1, num2)
    print(f"\n\t {comp}")

elif menu == 6:#Opcion Salir
    print("Gracias por usar este programa ¡bonito dia!")

else:
    print("Entrada inválida")
