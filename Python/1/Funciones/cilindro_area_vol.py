"""Programa que lee el radio y la altura de un cilindro, luego llama a las funciones y finalmente mostrar el área y volumen del cilindro. """

from math import *

def area_cilindro(r, a):
    area_c = (2*pi*r*a)+(2*pi*r**2)
    return area_c

def volumen_cilindro(r, a):
    vol_c = pi*r**2*a
    return vol_c

radio = float(input("Dame el radio de el cilindro: "))
altura = float(input("Dame la altura de el cilindro: "))

print(f"area = {area_cilindro(radio, altura):.2f}")
print(f"volumen = {volumen_cilindro(radio, altura):.2f}")