'''
Este programa indica si puedes entrar al Antro
Axel Jarquin Morga
ENTRADA:  edad
PROCESO:  Ir haciendo condicionales para validar RANGOS de edad
SALIDA: Mensaje de acuerdo con la edad
'''
print("Este programa indica si puedes entrar al antro")
edad = int(input("¿Cuantos años tienes? "))
if edad <= 0:
    print("Edad invalida")
elif edad <= 17:
    print("Eres menor de edad, se vale equivocarse, diviertete")
elif edad <= 30:
    print("Eres mayor de edad, se congruente, diviertete en el ANTRO")
elif edad <= 125:
    print("Te recomiendo el piano bar de la esquina")
else:
    print("Edad invalida")
