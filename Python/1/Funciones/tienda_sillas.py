""" En una tienda de sillas para oficina se venden de 3 tipos: básica, estándar y de lujo.
Además existen los clientes normales y los clientes frecuentes.

El precio de las sillas es:
- Básica $700.00 c/u
- Estándar $900.00 c/u
- De Lujo $1, 500.00 c/u

El dueño de la tienda ha decidido dar un descuento del 20% a los clientes frecuentes

Además ha decidido aplicar la siguiente política de descuentos por mayoreo a los clientes normales:
- si su compra es >= $10, 000 y < $20, 000 un 10% de descuento
- si su compra es >= $20, 000 un 15% de descuento

Escribe un programa que lea el tipo de silla (que es una letra mayúscula que puede ser B, E, L), el tipo de cliente (que es una letra mayúscula que puede ser F o N) y la cantidad a comprar (que es un número entero). Supón que solo se va a comprar de un tipo de silla.
El programa debe calcular y mostrar los siguientes datos (los datos son flotantes y debes mostrar uno en cada renglón):

- el precio antes de aplicar descuento,
- la cantidad de dinero que se otorga por descuento y
- el total a pagar por el cliente. """

def precio_antes(silla, cantidad):
    if silla == "B":
        precioa = 700*cantidad
    elif silla == "E":
        precioa = 900*cantidad
    elif silla == "L":
        precioa = 1500*cantidad
    return precioa

def descuento_a(cliente, precioa):
    if cliente == "F":
        descuento = precioa*0.2
    elif cliente == "N":
        if precioa <= 10000:
            descuento = 0
        elif precioa < 20000:
            descuento = precioa*0.1
        else:
            descuento = precioa*0.15
    return descuento

silla = input()
cliente = input()
cantidad = int(input())

precio_A = precio_antes(silla, cantidad)
descuento = descuento_a(cliente, precio_A)
total_pago = precio_A-descuento

print(precio_A)
print(descuento)
print(total_pago)
