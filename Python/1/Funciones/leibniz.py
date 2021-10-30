""" En matemáticas, la fórmula de Leibniz para el cálculo de π, nombrada así en honor a Gottfried Leibniz, dice que:

1 - 1/3 + 1/5 - 1/7 + 1/9 ... = π ⁄ 4

La expresión anterior es una serie infinita denominada serie de Leibniz, que converge a π ⁄ 4. También se la denomina serie de Gregory-Leibniz para reconocer el trabajo de James Gregory, contemporáneo de Leibniz.(Recuperado de: https://es.wikipedia.org/wiki/Serie_de_Leibniz).

Desarrolla un programa que contenga una función en Python que reciba un número entero positivo diferente a cero que representa la cantidad de términos a calcular de la serie, muestre la secuencia de términos que se van generando y regrese el resultado de la serie. """

def serie_leibniz(ctd_terminos):
    # Desarrolla la función
    t = 0
    d = 1
    for cont in range(1, ctd_terminos+1):
        if cont%2 == 0:
            t -= 1/d
        else:
            t += 1/d
        d += 2
    return t


def main():
    numero = int(input())
    #Se llama a la función que deberás implementar
    total = serie_leibniz(numero)
    text = ""
    d = 1
    cont = 1
    while cont <= numero:
        if cont == 1:
            text += "1"
        elif cont%2 == 0:
            text += "-1/"+str(d)
        else:
            text += "+1/"+str(d)
        d += 2
        cont += 1
    print(text, f" = {total:.2f}")

main()
