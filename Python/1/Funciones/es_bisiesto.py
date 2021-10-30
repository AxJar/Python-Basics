
"""Programa en el cual definas la función es_bisiesto().
Esta función debe recibir un número entero que representa un año, y te debe regresar True si el año es bisiesto, y False en caso contrario.
Recuerda que un año es bisiesto si es divisible entre 4, excepto cuando es divisible entre 100.
Aquellos años que son divisibles entre 100 no son bisiestos, a menos que sean divisibles entre 400. """

def es_bisiesto(y):
    if a%4 == 0 and a%100 != 0:
        return True
    elif a%100 == 0 and a%400 == 0:
        return True
    else:
        return False

a = int(input())
a_year = es_bisiesto(a)
print(a_year)