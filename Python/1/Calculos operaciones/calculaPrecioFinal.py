cant_articulos = int(input())
precio = float(input())
subtotal = cant_articulos * precio
impuestos = subtotal * 0.16
total = subtotal + impuestos
print(subtotal)
print(impuestos)
print(total)
