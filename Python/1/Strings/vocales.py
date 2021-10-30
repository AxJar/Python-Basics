'''
Programa que recibe del usuario una cadena (string) y nos indica cuántas
vocales tiene.
'''
palabra = input()
pa_m = palabra.lower()
suma = pa_m.count("a") + pa_m.count("e") + pa_m.count("i") + pa_m.count("o") + pa_m.count("u")
print(f"Tu palabra tiene {suma} vocales")
