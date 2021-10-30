def captura_secuencial():
    cont = 1              # Solo se usa contador porque quiero una lista secuencial
    matriz = []           # LISTA que tendra listas adentro
    for i in range(3):
        lista = []        # lista = renglón dentro de la matriz
        for j in range(3):
            lista.append(cont)       # Voy llenando la lista
            cont += 1
        matriz.append(lista)         # Le pego la lista a la matriz
    return matriz

def captura_usuario(r, c):
    matriz = []
    for i in range(r):
        lista = []
        for j in range(c):
            dato = int(input(f"Dame el dato para la posición {[i]}{[j]}: "))
            lista.append(dato)         # Hago un append del dato para guardarlo en la lista
        matriz.append(lista)           # Hago un append para guardar la LISTA en la matriz
    return matriz

def imprime_matriz(m):       # Recibe la matriz en m
    for r in range(len(m)):             # Se obtiene el tamaño de la matriz con len
        for c in range(len(m[r])):       # Se obtiene el tamaño del renglón
            print(m[r][c], end = "\t")     # Se imprime por renglón
        print()            # < enter > para el cambio del renglón

def imprime_elementos(m):          # Impresion por valores
    for r in m:                    # Usamos el comando "in" en "m"
        for valor in r:                # Se imprime el valor DENTRO de cada renglón
            print(valor, end = "\t")      # Se imprime VALOR por valor
    print()

def suma_matriz(m):
    suma = 0
    for lista in m:
        for valor in lista:
            suma = suma + valor
    print(f"La suma de los valores dentro de la matriz es {suma}")

def cambia_negativos(m):
    for i in range(len(m)):             # Con esto se sabe cuantas listas tiene la matriz
        for j in range(len(m[i])):      # Obtiene cuantos valores hay dentro de cada lista
            if m[i][j] > 0:
                m[i][j] = m[i][j] * -1
    return m

def suma_columnas(m):
    for i in range(len(m[0])):
        total = 0
        for j in range(len(m)):
            total += m[j][i]
        print(f"La suma de la columna {i} es {total}")


# Programa principal
print("Este programa manipula matrices")
ren = int(input("Cuantas listas tendra tu matriz? "))
col = int(input("Cuantos elementos tendra cada lista? "))
ma_secuencial = captura_secuencial()
print(*ma_secuencial, sep = "\n")
print()
matriz_usuario = captura_usuario(ren, col)
# print(*matriz_usuario, sep = "\n")
print()
imprime_matriz(matriz_usuario)
print()
imprime_elementos(matriz_usuario)
print()
suma_matriz(matriz_usuario)
# matriz_negativa = cambia_negativos(matriz_usuario)
# imprime_matriz(matriz_negativa)

print()

suma_columnas(matriz_usuario)
