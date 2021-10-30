f = open("../Manejo_archivos_python/answers.csv", "r")
respuestas = []           # Lista donde voy a guardar cada renglón del archivo
for renglon in f:
    respuestas.append(renglon)
    print(repr(renglon))
f.close()                 # Cerrar el archivo origen

lista = []
for dato in respuestas:
    lista.append(dato.strip().split(","))
print(*lista, sep = "\n")

llave = ["D","B","D","C","C","D","A","E","A","D"]
print("\t Numero de Estudiante \t   Numero de aciertos")
print("\t --------------------------------------------")
encabezado = "No. Estudiantes, No. Aciertos\n"              # Títulos de columna en Excel
with open("../resultadosExamen.csv","w") as outputFile:
    outputFile.write(encabezado)
    for i in range(len(lista)):
        resultados = ""
        correctas = 0
        for j in range(len(lista[i])):
            if lista[i][j] == llave[j]:
                correctas += 1
        print(f"\t\t{i+1}\t\t\t{correctas}")
        resultados = resultados + str(i + 1) + "," + str(correctas) + "\n"
        outputFile.write(resultados)

