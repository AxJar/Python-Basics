"""
Este programa te arroja los precios de envio dependiendo de los kg y te da la suma de las ganacias
Made by:Axel Jarquin Morga
"""
# Funciones a utilizar

def calcula_costo(kg):
    if kg < 15:
        c = 1200
    elif kg < 50:
        c = 1200 + (kg - 15) * 50
    elif kg <= 90:
        c = 2700 + (kg - 50) * 30
    else:
        c = 3500 + (kg - 90) * 20
    return c

# Programa Principal

total = 0
kilos = int(input("Cuanto pesa su paquete? "))

while kilos > 0:

    costo = calcula_costo(kilos)
    print(f"El costo de su envio es: {costo} pesos")
    total = total + costo
    kilos = int(input("Cuanto pesa su paquete? "))

print(f"Las ganancias del dia fueron ${total}. ")