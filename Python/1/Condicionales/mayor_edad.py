'''
Este programa indica si ya eres mayor de edad
Axel Jarquin Morga
ENTRADA:  edad
PROCESO:  Pido la edad y la guardo en la variable edad
          Comparo edad >= 18 entonces "Eres mayor de edad"
          Sino "Eres menor de edad"
SALIDA: "Eres mayor de edad"/"Eres menor de edad"
'''
print("Este programa indica si eres mayor de edad")
edad = int(input("¿Cuantos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")