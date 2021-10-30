'''
De una lista definida de strings, determinar cuántas de éstas empiezan con la letra que te indique el usuario.
'''
lista = ["lunes", "martes", "miércoles" "jueves","viernes"]
letra = input("Dime la letra ")
cont = 0
for elemento in lista:
    if elemento.startswith(letra):
        cont+=1

print(cont)
