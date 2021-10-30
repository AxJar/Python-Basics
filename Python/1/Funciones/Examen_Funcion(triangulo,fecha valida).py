# Axel Jarquin Morga
# Lucia Loy


def area_triangulo(b, alt):#funcion triangulo
    a = (b*alt)/2
    return a

def fecha_valida(d, m, a):#Funcion fecha valida
    if 0 < m <= 12:
        if d >= 1 and d <= 31:
            if a > 0 and a <= 2020:
                  print("Fecha válida")
            else:
                 print("Fecha inválida")
        else:
            print("Fecha inválida")
    else:
        print("Fecha inválida")


# PROGRAMA PRINCIPAL

print("MENU DE FUNCIONES \n ")
print("1. Area de un triángulo rectángulo")
print("2. Fecha válida")
print("3. Salir")

menu = int(input("Elige la opción del menu que deseas consultar: "))
if menu == 1:
    base = float(input("Ingresa la base en cm: "))
    altura = float(input("Ingresa la altura en cm: "))
    area = area_triangulo(base, altura)
    print(f"El área del triángulo es de {area:.2f} cm2")
elif menu == 2:
    dia = int(input("Ingresa el día en numero: "))
    mes = int(input("Ingresa el mes en numero: "))
    año = int(input("Ingresa un año entre 0 y 2020: "))
    fecha_valida(dia, mes, año)
elif menu == 3:
    print("Gracias por usar este programa")
else:
    print("Entrada inválida")