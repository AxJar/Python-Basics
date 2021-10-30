"""Programa que recibe del usuario una lista y devuelva otra con los elementos de la lista original, pero sin elementos duplicados. """

"""
Entradas
Se recibe un número entero positivo correspondiente al número de elementos que el usuario ingresará.
Se reciben uno a uno y por renglón, los elementos de la lista (strings y de acuerdo al número recibido anteriormente).

Salidas
Si el valor correspondiente al número de elementos que tendrá la lista es 0 o negativo se deberá mandar el mensaje “Error”.
Si el valor recibido es mayor a 0, se despliega la lista original (después de haber recibido los datos). Posteriormente se despliega la lista pero sin duplicados.

Ejemplos de ejecución del programa
 >  >  > 4
 >  >  > Pedro
 >  >  > Gerardo
 >  >  > Hugo
 >  >  > Pedro
['Pedro', 'Gerardo', 'Hugo', 'Pedro']
['Pedro', 'Gerardo', 'Hugo']

 >  >  > 0
"Error"
"""

""" l = []
elementos = int(input())
for i in range(elementos):
    dato = str(input())
    l.append(dato)

if elementos <= 0:
    print("Error")
else:
    print(l)
    print(list(set(l))) """

num = int(input())
if num > 0:
    lis = []
    for i in range(num):
        per = input()
        lis.append(per)
    print(lis)
    for a in range(len(lis)):
        cont = 0
        for b in range(len(lis)):
            try:
                if lis[a] == lis[b]:
                    cont += 1
                    if cont > 1:
                        lis.pop(b)
            except:
                break
    print(lis)
else:
    print("Error")