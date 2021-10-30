
""" Escribe un programa que convierta pies, pulgadas y yardas a centímetros, para lo cual debes definir 3 funciones:
- Función que reciba una cantidad de pies (entero positivo) y devuelva el equivalente a centímetros.
- Función que reciba una cantidad de pulgadas (entero positivo) y devuelva el equivalente a centímetros.
- Función que reciba una cantidad de yardas (entero positivo) y devuelva el equivalente en centímetros. """

# Función conversión de pies a centímetros.
def pies_a_cm (p):
    return p * 30.48   # Un pie equivale a 30.48 centímetros.

def inches_a_cm (i):
    return i * 2.54    # Una pulgada equivale a 2.54 centímetros.

def yarda_a_cm (y):
    return y * 91.44

# PROGRAMA PRINCIPAL

menu = int(input("Elige que quieres convertir\n\t1.Pies a cm\n\t2.Pulgadas a cm\n\t3.Yardas a cm\n\t "))
if menu == 1:
    pies = int(input())
    p_cm = pies_a_cm (pies)
    if pies > 0:
        print(f"{p_cm:.2f}")
    else:
        print("Error")

elif menu == 2:
    inches = int(input())
    i_cm = inches_a_cm (inches)
    if inches > 0:
        print(f"{i_cm:.2f}")
    else:
        print("Error")

elif menu == 3:
    yardas = int(input())
    yarda_cm = yarda_a_cm (yardas)
    if yardas > 0:
        print(f"{yarda_cm:.2f}")
    else:
        print("Error")
else:
    print("Error")