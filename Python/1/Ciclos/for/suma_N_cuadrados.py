
""" Escribe un programa que reciba un número entero y calcule la suma: 12 + 22 + 32 +...+"numero2".
Donde "numero" es el valor que el usuario proporcionó. Finalmente se imprime el resultado de la suma en pantalla.
"""

n = int(input())
suma = 0
for i in range (n+1):
    num = i**2
    suma = suma+num
print(suma)