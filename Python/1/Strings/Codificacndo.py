'''Genere otro String en el cual cambies las letras t por 7, i por 1, las letras a por * y la e por 3 y se despliegue dicho string cambiado a pantalla.
'''

frase = input("Dame una frase celebre: ")

# con esto se modifican las letras
modificada = frase.lower()
modificada = modificada.replace("t", "7")
modificada = modificada.replace("i", "1")
modificada = modificada.replace("a", "*")
modificada = modificada.replace("e", "3")
print(modificada)

# lista=list(frase) list convierte TODO a listas
lista = frase.split()
print(lista)
print(f"tu frase tiene {len(lista)} palabras")
cont = 0
for palabra in lista:
    if len(palabra) > 5:
        cont += 1
print(f"Tu frase tiene {cont} palabras con mas de 5 letras")
