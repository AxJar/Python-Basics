"""Programa que solicita números enteros hasta que el número ingresado sea un número negativo.
El programa muestra cuántos números ingresados fueron pares. """

num = 0
contPares = 0
while num >= 0:
    num = int(input())
    pares = num % 2
    if pares == 0 and num >= 0:
        contPares += 1
print("Total de pares = ", contPares)
