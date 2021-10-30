""" Escriba un programa que simule el juego Piedra, papel, tijera para dos jugadores (Ana y Juan).

Las reglas del juego son las siguientes:

-- Simultáneamente, los dos jugadores muestran una mano en tres posibles posiciones:
-- Piedra: se muestra el puño cerrado y se representa con un caracter 'a'.
-- Papel: se muestra la palma de la mano y se representa con un caracter 'p'.
-- Tijera: se muestra la palma de la mano con los dedos separados en dos grupos y se representa con un caracter 't'.
-- El jugador que ha sacado Piedra gana al jugador que ha sacado Tijera.
-- El jugador que ha sacado Tijera gana al jugador que ha sacado Papel.
-- El jugador que ha sacado Papel gana al jugador que ha sacado Piedra.
-- Caso de empate cuando dos jugadores elijan el mismo elemento. """

ana = str(input())
juan = str(input())
if len(ana) == 1 and len(juan) == 1:
    if(ana == "a" or ana == "p" or ana == "t") and (juan == "a" or juan == "p" or juan == "t"):
        if ana == "a" and juan == "t":
            print("Gana Ana")
        elif juan == "a" and ana == "t":
            print("Gana Juan")
        elif ana == "t" and juan == "p":
            print("Gana Ana")
        elif juan == "t" and ana == "p":
            print("Gana Juan")
        elif ana == "p" and juan == "a":
            print("Gana Ana")
        elif juan == "p" and ana == "a":
            print("Gana Juan")
        else:
            print("Empate")
    else:
        print("Tirada incorrecta")
else:
        print("Las tiradas deben ser un carácter")