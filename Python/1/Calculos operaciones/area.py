'''
Este programa obtiene el area de un circulo dado el radio
AUTOR:Axel Jarquin Morga
ENTRADAS:rad
PROCESO:Solicitar el radio y guardarlo en su variable correspondiente.
        Multiplicar pi por el radio elevado al cuadrado
        Imprimir resultado
SALIDAS:area_circulo
'''
from math import *
print("Este programa obtiene el area de un circulo dado el radio")
rad = float(input("Ingrese el radio de su circulo "))
area_circulo = pi*pow(rad, 2)
print(f" El area del circulo es {area_circulo:.2f}" )
