"""
Axel Jarquin Morga  //  A01636324
Examen Integrador
"""

"""Esta función nos da la suma de los productos que se venden en la semana"""
def sales_t(m):
    sales = 0
    for renglon in m:
        sales += sum(renglon)
    return sales

"""Esta función nos dice que producto vale la pena dejar de vender"""
def p_d_v(m):
    minimum = total_sales
    product = 0
    for a in range(len(m)):
        sale = 0
        for e in range(len(m[a])):
            sale += m[a][e]
        if sale < minimum:
            minimum = sale
            product = a + 1
    print(f"2. El producto que vale la pena dejar de vender es el {product}")

"""Esta función nos dice de qué producto vale la pena tener más inversión"""
def p_v_m(m):
    maximum = total_sales
    product = 0
    for a in range(len(m)):
        sale = 0
        for e in range(len(m[a])):
            sale += m[a][e]
        if sale > maximum:
            maximum = sale
            product = a + 1
    print(f"3. El producto que vale la pena tener más inversión es el {product}")

"""Esta función nos dice qué día de la semana le conviene dedicarse a sus tareas de casa en lugar de salir a vender."""
def d_m(m):
    week = [0,0,0,0,0]
    for a in range(len(m)):
        for x in range(len(m[a])):
            week[x] += m[a][x]
    minimum = total_sales
    day = 0
    for e in range(len(week)):
        if week[e] < minimum:
            minimum = week[e]
            day = e + 1
    print(f"4. El dia de la semana que le conviene dedicarse a sus tareas de casa en lugar de salir a vender es el {day}")

"""Las contraseñas tienen que tener 5 requisitos, pero solo validara los 2 primeros
1. Tienen más de 8 caracteres de longitud.
2. Utilizan una combinación de minúsculas y mayúsculas, números y caracteres especiales (como
~!@#$%^&*()_+=?><.,/).
"""
def password_validation(p):
    if len(p) <= 8:
        requirement1 = False
    else:
        requirement1 = True
    characters = "~!@#$%^&*()_+=?><.,/"
    numbers = "1234567890"
    if (p.islower() == True) or (p.isupper() == True):
        requirement2 = False
    else:
        requirement2 = True
    for listt in p:
        if listt not in numbers:
            requirement3 = False
        else:
            requirement3 = True
            break
    for listt in p:
        if listt not in characters:
            requirement4 = False
        else:
            requirement4 = True
            break
    if (requirement1 == True) and (requirement2 == True) and (requirement3 == True) and (requirement4 == True):
        print(f"\n\tLa clave {p} cumple con los 2 primeros requisitos de PayPal")
    else:
        print(f"\n\tLa clave {p} no es válida como contraseña segura en PayPal")

sales= [[7, 15, 8, 9, 1],
          [3, 20, 16, 20, 7],
          [8, 7, 6, 6, 6],
          [15, 18, 13, 19, 11],
          [11, 13, 5, 19, 2]]
total_sales = sales_t(sales)

while True:
    print("""
    Menu:

    (1) Análisis de datos Ventas Juanita
    (2) Clave para compras por internet
    (3) Salir""")
    opcion = int(input("\n\tEscoge una opción del menu: "))
    if opcion == 1:
        print(f"1. El total de ventas de esta semana fue de {total_sales} productos")
        p_d_v(sales)
        p_v_m(sales)
        d_m(sales)
    elif opcion == 2:
        password = input("\n\tIngresa tu clave de PayPal: ")
        password_validation(password)
    elif opcion == 3:
        print("\n\tHasta la próxima")
        break