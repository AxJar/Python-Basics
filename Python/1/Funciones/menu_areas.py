'''
Este programa usa funciones
Axel 2020
1. LLAMADO A LIBRERIA
2. DEFINICIÓN DE FUNCIÓN
3. Solicito entradas
4. Realizo procesos o calculos
5. Presento salidas
'''
from math import *


def area_circulo(r):
    a = pi*r**2
    return a


def area_rectangulo(b, alt):
    a = b*alt
    print("El area del rectangulo es ", a)


# Programa principal
print("Este programa trabaja con funciones")
radio = float(
    input("Dame el radio en cm, para obtener el area de un circulo "))
area = area_circulo(radio)
print(f"Para un circulo con radio {radio:.2f} el area es {area:.2f} cm2")
base = float(
    input("Dame el valor de la base en cm, para obtener el area de un rectángulo "))
altura = float(input("Y ¿Cual es la altura (también en cm por favor)? "))
area_rectangulo(base, altura)
