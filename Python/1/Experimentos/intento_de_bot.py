'''
Patricio Baeza Rubin de Celis
A00830421
Examen integrador
'''

import random
seguir = 'q'

texto = open("../Manejo_archivos_python/preguntas.txt", "r")
PyR = texto.readlines()
texto.close()

print('Bienvenido al examen integrador')
name = input('Nombre del alumno: ')
saludo = input('Introduzca un mensaje: ')
saludoL = saludo.lower()
if saludoL == 'hola' or saludo == 'que tal' or saludo == 'buen dia':
    print(random.choice(['Hola que tal?', 'Buen dia', 'Hola que puedo hacer por ti?', 'Que tal', '¿En que te puedo ayudar?', 'Hola, ¿Como estas?', 'Hello', '¿Que tal mi nombre es TC1028']))



while seguir == 'q':
    p = input('Ingrese su pregunta: ')
    if p == PyR[0][2:-1] or p == PyR[0][3:-1] or p == PyR[0][2:-1].lower():
        print(PyR[1][2:])
    elif p == PyR[2][2:-1] or p == PyR[2][3:-1] or p == PyR[2][2:-1].lower():
        print(PyR[3][2:])
    elif p == PyR[4][2:-1] or p == PyR[4][3:-1] or p == PyR[4][2:-1].lower():
        print(PyR[5][2:])
    elif p == PyR[6][2:-1] or p == PyR[6][3:-1] or p == PyR[6][2:-1].lower():
        print(PyR[7][2:])
    elif p == PyR[8][2:-1] or p == PyR[8][3:-1] or p == PyR[8][2:-1].lower():
        print(PyR[9][2:])
    elif p == 'Adios' or p == 'adios':
        seguir = 'w'
    else:
        print('No puedo contestar esa pregunta :(')
print('Vuelva pronto')


