"""
Este programa recibe 2 cadenas que representan 2 palabras, y da como salida una combinación de las palabras recibidas.
La primera palabra de salida  comienza con la primera mitad del primer string y termina con la segunda mitad del
segundo string,La segunda palabra de salida comienza con la segunda mitad del primer string y termina con la
primera mitad del segundo string.
"""

pal1 = input()
pal2 = input()
can_pal1 = len(pal1)
can_pal2 = len(pal2)

if can_pal1 % 2 == 0:
    a = int(can_pal1 / 2)
else:
    a = int(can_pal1 / 2 + 0.5)
if can_pal2 % 2 == 0:
    b = int(can_pal2 / 2)
else:
    b= int(can_pal2 / 2 + 0.5)

print(pal1[0:a] + pal2[b:])
print(pal1[a:] + pal2[0:b])
