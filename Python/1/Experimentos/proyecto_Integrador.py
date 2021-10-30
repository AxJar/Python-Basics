"""
Proyecto Integrador
María Fernanda Flores Salas
A01634543
Este programa consiste en un juego cuyo propósito es apoyar a jóvenes en
el estudio de la smatématicas. Le asigna al usuario una cantidad de "monedas"
las cuales utilizará para jugar, con la oferta de invertir para ganar más
pero con la posibilidad de perder la inversión. El juego como tal es un
banco de preguntas de ecuaciones con variables las cuales el usuario deberá
despejar. Las preguntas continuarán, sumando o restando al dinero del
usuario hasta que este decida salir.
"""
def despedida(n,i,b):
    print(f"El día de hoy resolviste {i} ecuaciones {n}.")
    if b>100:
        ganancia=b-100
        print(f"¡Felicidades {n} vas muy bien! Tienes un saldo de {b}, lo que quiere decir que has obtenido una ganancia de {ganancia} en {i} intentos.\n Sigue así y vuelve pronto")
    elif b<100:
        perdida=100-b
        print(f"Tu banco tiene un saldo de {b}, lo que quiere decir que has sufrido una pérdida de {perdida} monedas, pero no te preocupes {n}, sigue practicando y podrás recuperar tus monedas y obtener muchas más.\nRegresa pronto.")
    else:
        if i==0:
            print(f"Tu banco cuenta con 100 monedas que no has utilizado. Gástalas para practicar ecuaciones y podrás ver tu saldo crecer.\nVuelve pronto a practicar.")
        else:
            print(f"Tienes 100 monedas en el banco, te has mantenido estable a lo largo de {i} ecuaciones.\nNo olvides practicar y vuelve pronto.")
        
p=open("ecuaciones.csv","r")
preguntas=[]    
for renglon in p:
    preguntas.append(renglon)
p.close 

lista=[]
for dato in preguntas:
    repr(dato)
    lista.append(dato.strip().split(","))
    
r=open("valores.csv","r")
resp=[]    
for renglon in r:
    resp.append(renglon)
r.close 

listaresp=[]
for dato in resp:
    repr(dato)
    listaresp.append(dato.strip().split(","))


banco=100
nombre=input("Bienvenido, ¿cuál es su nombre? \n")
print(f"Mucho gusto {nombre}, este es un juego que te ayudará a estudiar matemáticas. \nEn este momento se han depositado 100 monedas en tu banco. \nCon estas monedas pagarás para ver cada pregunta, tú decides cuanto invertirás, pues de acertar, se duplicará tu inversión, pero de equivocarte perderás dicha inversión.")
print("Comencemos, ingresa la opción que desees")

while True:
    print("\n\t\t\t\t\t\tMENÚ \n\n1. Resolver operaciones \t\t2. Consultar banco \t\t3. Salir\n")
    opcion=int(input())
    intentos=0
    
    if opcion==1:
        
        inversion=int(input("¿Cuánto deseas invertir para esta ecuación? "))
        if inversion>0 and inversion<=banco:
            print(f"Has decidido invertir {inversion} monedas, si contestas esta ecuación correctamente se duplicará, si no lo perderás.\n")
            banco=banco-inversion
            print("Resuelve para el valor de x. Ingresa tu respuesta sin espacios o comas.\nSi la ecuación es con fracciones ingresa tu respuesta con fracciones, \nsi es en decimales, ingresa los primeros cuatro decimales sin redondear.")
            
            for i in range(len(lista)):
                correctas=0
                incorrectas=0
                for j in range(len(lista[i])):
                    print(lista[i][j])
                    respuesta=input("x tiene un valor de: ")
                    if listaresp [i][j]==respuesta:
                        inversion=inversion*2
                        banco=banco+inversion
                        print(f"¡Respuesta correcta! Tu balance en el banco es de {banco} monedas.")
                        correctas+=1
                    else:
                        banco=banco-inversion
                        print(f"Respuesta incorrecta. Tu balance en el banco ahora es de {banco} monedas. Continúa estudiando para obtener más monedas.")
                        incorrectas+=1
                intentos+=1
        elif inversion<=0:
            print("Valor inválido de inversión, ingresa un valor positivo a invertir.")
        elif inversion>banco:
            print("No tienes tantas monedas en el banco, intenta con una menor inversión.")
        
    elif opcion==2:
        print(f"Tu estado de cuenta es de {banco}.\nAl invertir, gastarás algo de tu crédito, pero si lo haces inteligentemente obtendrás ganancias.")
        
    elif opcion==3:
        despedida(nombre,intentos,banco)
        break
    
    else:
        print("Opción no válida.")
