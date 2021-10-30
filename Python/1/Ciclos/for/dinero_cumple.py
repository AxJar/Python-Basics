""" Los padres de un niño le regalarán $10 cuando cumpla "n" años, y cada cumpleaños doblarán la cantidad que le darán hasta que el obsequio exceda $1000.

Escribe un programa que lea el valor n, es decir, la edad en la que iniciará el regalo de $10 y muestre como salida la edad que tendrá el niño cuando reciba el último obsequio y la cantidad de dinero que recibirá en ese año."""

suma = 10
edad = int(input())
for i in range(edad, edad+7):
    suma = suma*2
print(f"{edad+7} {suma}")
