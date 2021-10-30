'''
Programa que recibe dos cadenas del usuario y nos dice cuál de las dos tiene más vocales.
'''
w1 = input()
w2 = input()
w1_m = w1.lower()
w2_m = w2.lower()
suma1 = w1_m.count("a") + w1_m.count("e") + w1_m.count("i") + w1_m.count("o") + w1_m.count("u")
suma2 = w2_m.count("a") + w2_m.count("e") + w2_m.count("i") + w2_m.count("o") + w2_m.count("u")
if suma1 > suma2:
    print(f"La primera palabra tiene mas vocales")
elif suma1 == suma2:
    print(f"Las 2 palabras tienen el mismo numero de vocales")
else:
    print(f"La segunda palabra tiene mas vocales")
