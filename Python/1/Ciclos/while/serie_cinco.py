""" Escribe un programa que lea los valores a y b y muestre una serie de números que empiezan en a y se incrementan de 5 en 5 hasta llegar a b.
Nota que a y b no necesariamente son múltiplos de 5, y que debe mostrar todos los números que sean <= b.
Supón que siempre se te dará un valor de a que sea menor que b. """

a = int(input())
b = int(input())
if a <= b:
    while a <= b:
        print(a)
        a += 5