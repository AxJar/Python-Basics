"""
Clave	Precio
 A	     120
 B	     250
 C	     360

Programa que lee la clave del artículo que va a comprar (nota que es letra mayúscula) o X si ya no quiere comprar más artículos.
El programa debe mostrar en la pantalla el precio correspondiente a cada artículo pedido, 
el programa debe repetirse mientras el usuario no teclee la clave X, cuando el usuario teclee
la clave X el programa debe mostrar en la pantalla el total de la compra del cliente."""

x = "A"
carrito = 0
def compra (a, b):
    xd = a+b
    return xd

while x == "A" or x == "B" or x == "C":
    x = input()
    if x == "A":
        carrito = compra(carrito, 120)
        print(120)
    if x == "B":
        carrito = compra(carrito, 250)
        print(250)
    if x == "C":
        carrito = compra(carrito, 360)
        print(360)
    else:
        x == "X"
print(carrito)

int(input())