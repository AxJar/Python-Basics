"""Axel Jarquin Morga    //    A01636324"""

""" Esta función devuelve , el alumno con mayor promedio """
def cali_alta(cf):
    alta = 0
    nombre = ""
    for elemento in cf:
        if alta < elemento[2]:
            alta = elemento[2]
            nombre = elemento[1]
    return nombre

""" Esta función devuelve , el alumno con menor promedio """
def cali_baja(cf):
    baja = 100
    nombre = ""
    for elemento in cf:
        if baja > elemento[2]:
            baja = elemento[2]
            nombre = elemento[1]
    return nombre

""" Esta función devuelve el promedio grupal """
def cal_promedio(ap):
    suma = 0
    for i in range(2,11):
        suma += ap[i]
    return suma / 9

""" Esta función devuelve a los alumnos que aprobaron el curso, es decir, calificaciones mayores a 60 """
def alumnos_aprobados(cf):
    print("\nALUMNOS APROBADOS\nID\tNombre\t\tCalificacion")
    for elemento in cf:
        if elemento[2] >= 60:
            print(f"{elemento[0]:5}\t{elemento[1]:15}{elemento[2]:5}")

""" Esta función devuelve a los alumnos que obtuvieron una calificacion menor a 60 , es decir , alumnos reprobados """
def alumnos_reprobados(cf):
    print("\nALUMNOS REPROBADOS\nID\tNombre\t\tCalificacion")
    for elemento in cf:
        if elemento[2] < 60:
            print(f"{elemento[0]:5}\t{elemento[1]:15}{elemento[2]:5}")

""" Esta función devuelve a los alumnos que obtuvieron una calificacion menor a 60 , es decir ,
alumnos reprobados y si el alumno reprobo el curso con menos de 45 pts , nos muestra si tiene o no derecho a extraordinario """
def alumnos_reprobados_extra(cf):
    print("\nALUMNOS REPROBADOS\nID\tNombre\t\tCalificacion\t  Extraordinario")
    for elemento in cf:
        if elemento[2] < 60:
            if elemento[2] < 45:
                extra = "N"
            else:
                extra = "S"
            print(f"{elemento[0]:5}\t{elemento[1]:15}{elemento[2]:5}\t\t\t{extra:5}")

def alu_repr_d_extra(cf):
    for pasada in range(len(cf)):
        for renglon in range(1,len(cf)):
            if cf[renglon][2]<cf[renglon-1][2]:
                temp = cf[renglon]
                cf[renglon] = cf[renglon-1]
                cf[renglon-1]=temp
    print("\nLa lista ordenada queda asi:\n")
    print("ID\tNombre\t\tCalificacion\tExtraordinario")
    for elemento in cf:
        if elemento[2] < 60:
            if elemento[2] < 45:
                extra = "N"
            else:
                extra = "S"
            print(f"{elemento[0]:8}{elemento[1]:15}{elemento[2]:10}\t\t{extra:10}")


def asc_desc_nombre(cf):
    for pasada in range(len(cf)):
        # Empezamos en 1 porque vamos a comparar con el anterior
        # Comparo el NOMBRE que esta en la posición 1
        for renglon in range(1,len(cf)):
            if cf[renglon][1] < cf[renglon-1][1]: # [1] es el nombre
                temp = cf[renglon]
                cf[renglon] = cf[renglon-1]  # Intercambiamos TODO el renglon
                cf[renglon-1] = temp
    print("\n La lista ordenada de alumnos queda asi: \n")
    print("ID   Nombre\t  Calificación\t")
    for elemento in calFinales:
        print(f"{elemento[0]:5}\t{elemento[1]:15}{elemento[2]:5}")


def asc_desc_cali(cf):
    for pasada in range(len(cf)):
        # Empezamos en 1 porque vamos a comparar con el anterior
        # Comparo el NOMBRE que esta en la posición 1
        for renglon in range(1,len(cf)):
            if cf[renglon][1] > cf[renglon-1][1]: # [1] es el nombre
                temp = cf[renglon]
                cf[renglon] = cf[renglon-1]  # Intercambiamos TODO el renglon
                cf[renglon-1] = temp
    print("\n La lista ordenada de alumnos queda asi: \n")
    print("ID   Nombre\t  Calificación\t")
    for elemento in calFinales:
        print(f"{elemento[0]:5}\t{elemento[1]:15}{elemento[2]:5}")



#  Experimento 1 : leer todos los registros y transformarlos en listas para manipularlas
listaAlumnos = []
with open("../Manejo_archivos_python/Calificaciones.csv", "r") as inputFile:
    header = inputFile.readline()
    listaActividades = header.strip().split(",")
    for line in inputFile:
        listaAlumnos.append(line)
""" print(repr(header))
print("\n")
for elemento in listaAlumnos:
    print(repr(elemento)) """

# Separamos cada una de las lineas en lista y convertimos los datos numéricos
nuevaLista = []
for elemento in listaAlumnos:
    nvoElemento = elemento.strip().split(",")
    nuevaLista.append(nvoElemento)
"""     print(nvoElemento) """

# El siguiente paso es convertir los dato numéricos
# El diccionario de datos dice que son las columnas 3 a 11
# Es decir, los indices 2 al 10
for elemento in nuevaLista:
    for columna in range(2,11):
        elemento[columna] = int(elemento[columna])
"""     print(elemento) """

# Vamos a sacar el promedio de cada alumno de acuerdo a las reglas definidas
alumnoPromedio = []
alumnoPromedio.append("99") # Agregamos el ID
alumnoPromedio.append("PROMEDIO") # Agregamos el nombre

#iteramos sobre filas y columnas para obtener el promedio
for columna in range(2,11):
    contador = 0      # Inicializamos las variables para los calculos
    promedio = 0
    suma = 0
    for elemento in nuevaLista:
        contador += 1
        suma += elemento[columna]
    promedio = suma / contador
    alumnoPromedio.append(int(promedio)) # Añadimos el promedio de cada columna al alumnoPromedio

indice = 2
mayor = 0
for columna in range(2,11):
    if alumnoPromedio[columna] > mayor:
        mayor = alumnoPromedio[columna]
        indice = columna

# Usamos el header para saber cual es la actividad con el promedio mas alto
# al final el promedio mas grande esta en mayor y la actividad es la actividad indice
print(f"\nLa actividad con el promedio mas alto es {listaActividades[indice]} con un valor de {mayor}\n")

# Vamos a ver que actividad tuvo el promedio mas bajo
indice = 2 # Comenzamos de nuevo desde la columna 2
menor = 100 # Ponemos el promedio máximo posible

for columna in range(2,11):
    if alumnoPromedio[columna] < menor:
        menor = alumnoPromedio[columna]
        indice = columna
# Imprimimos el resultado
print(f"La actividad con el promedio mas bajo fue {listaActividades[indice]} con un valor de {menor}\n")

calFinales = [] # Comenzamos con una nueva lista vaciá

for elemento in nuevaLista:
    alumnoFinal = [] # Lista vaciá para generar las calificaciones por alumno
    # Copiamos el nombre y el ID
    alumnoFinal.append(elemento[0])
    alumnoFinal.append(elemento[1])
    # Las tareas están de la columna 2 a la 6
    suma = 0
    promedio1 = 0
    contador = 0
    for columna in range(2,7):
        suma += elemento[columna]
        contador += 1
    promedio1 = suma / contador
    # Los exámenes rápidos van de la columna 7 a la 9
    suma = 0
    promedio2 = 0
    contador = 0
    for columna in range(7,10):
        suma += elemento[columna]
        contador += 1
    promedio2 = suma / contador
    # Una vez que tenemos los dos promedios, calculamos la calificación final usando
    # Las ponderaciones // 30: tareas (promedio) // 30: exámenes rápidos (promedio2) // 40:Examen Final
    promedioFinal = int( (promedio1*.3) + (promedio2*.3) + (elemento[10]*.4) )
    # Finalmente, añadimos la calificación final a la lista de calificaciones
    alumnoFinal.append(promedioFinal)
    calFinales.append(alumnoFinal)
print("ID   Nombre\t  Calificación")
for elemento in calFinales:
    print(f"{elemento[0]:5}{elemento[1]:15}{elemento[2]:5}")

while True:
    print("""
    Menu:
    (1) Alumno con calificacion mas alta
    (2) Alumno con calificacion mas baja
    (3) Promedio grupal de calificaiones finales
    (4) Alumnos aprobados
    (5) Alumnos reprobados
    (6) Alumnos que cuentan con derecho a examen
    (7) Ordena la lista de alumnos por nombre, ascendente y descendente
    (8) Ordena la lista de alumnos por calificaciones finales, ascendente y descendente
    (9) Ordena la lista de alumnos reprobados, primero quienes no tienen derecho a extraordinario y luego los que si
    (10) Salir
    """)
    opcion = int(input("Escoge una opción del menu: "))
    if opcion == 1:
        print("\nEl alumno que obtuvo la calificacion mas alta fue ",cali_alta(calFinales))
    elif opcion == 2:
        print("\nEl alumno que obtuvo la calificacion mas baja fue ",cali_baja(calFinales))
    elif opcion == 3:
        print(f"\nEl promedio grupal es de {cal_promedio(alumnoPromedio):.2f}")
    elif opcion == 4:
        alumnos_aprobados(calFinales)
    elif opcion == 5:
        alumnos_reprobados(calFinales)
    elif opcion == 6:
        alumnos_reprobados_extra(calFinales)
    elif opcion == 7:
        asc_desc_nombre(calFinales)
    elif opcion == 8:
        asc_desc_cali(calFinales)
    elif opcion == 9:
        alu_repr_d_extra(calFinales)
    elif opcion == 10:
        print("Gracias por usar este programa!")
        break
    else:
        print("\nEsta opcion no es valida, intenta de nuevo")

# Para poder escribir el archivo, necesitamos convertir cada una de las filas a un string
# Vamos a usar el método largo
headerCalificaciones = "ID,Nombre,Calificaciones,Extraordinario\n"  # Este sera el header del archivo
# Abrimos el archivo para escritura
with open("../Manejo_archivos_python/calificacionesFinales.csv","w") as outputFile:
    outputFile.write(headerCalificaciones)
    # Convertimos cada linea en string y le agregamos las comas y el salto de linea
    for elemento in calFinales:
        alumnoString = ""
        # Añadimos ID y nombre que ya son strings
        alumnoString += elemento[0] + "," + elemento[1]
        for columna in range(2,len(elemento)):
            alumnoString += "," + str(elemento[columna])
            if elemento[columna] < 60:
                if elemento[columna] <45:
                    extra = "N"
                else:
                    extra = "S"
                    alumnoString += "," + extra
        alumnoString += "\n"
        outputFile.write(alumnoString)
