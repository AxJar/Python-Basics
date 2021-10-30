"""Programa que recibe un entero y devuelva True si es un número primo y False si NO es un número primo.
Asume que los números negativos pueden ser primos """

num = int(input())
div = 1
cont = 0


if num > 0:
    while div <= num:
        p_np = num%div
        if p_np == 0:
            cont = cont+1
            div = div+1
        else:
            div = div+1

elif num < 0:
    while -div >= num:
        p_np = num%div
        if p_np == 0:
            cont = cont+1
            div = div+1
        else:
            div = div+1

if cont == 2:
    print("True")
else:
    print("False")