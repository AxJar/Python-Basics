def cambia_vocales():
    frase = input("Teclea una frase: ")
    nuevo_string = ""
    for letra in frase:
        if letra in "eiouEIOUéíóú":
            nuevo_string = nuevo_string + "a"
        else:
            nuevo_string = nuevo_string + letra
    print(nuevo_string)
    print(frase)

def cambia_vocales_indice():
    frase = input("Teclea una frase: ")
    lis = list(frase)                              # Se usa la función list para convertir a lista
    print(lis)
    for i in range(len(lis)):
        if lis[i] in "eiouEIOUéíóú":
            lis[i] = "a"
    texto = "".join(lis)
    print(texto)

# Programa principal
# cambia_vocales()
cambia_vocales_indice()
