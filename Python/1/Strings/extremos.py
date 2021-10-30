'''
Este programa recibe un string y regresa un string construido por los primeros
dos y los últimos dos caracteres del string original.
Si la longitud del string que recibe, es menor a dos, regresa un string vacío.
'''
palabra = input()
l_palabra = len(palabra)

if l_palabra < 2:
    print("")
else:
    print(palabra[0:2]+palabra[-2:])
