""" Escribir un programa en Python que lea un string y muestre fragmentos de este. """

cadena = input()
print(len(cadena))
print(cadena[0])
print(cadena[-1])
impar = ""
for i in range(len(cadena)):
    if i % 2 != 0:
        impar = impar + cadena[i]
print(impar)