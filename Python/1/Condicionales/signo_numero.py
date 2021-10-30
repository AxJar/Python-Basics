""" Identifica si un número entero es positivo, negativo o cero. """

num = int(input("Dame el numero que quieres identificar si es , positivo , negativo o cero: "))
if num > 0:
    print("Tu numero es positivo")
else:
    if num == 0:
        print("Cero")
    else:
        if num < 0:
            print("Tu numero es negativo")