def precio_hamb(tipo, queso):

    if tipo == "C":
        precio = 75
    elif tipo == "P":
        precio = 60

    if queso == "S":
        precio = precio + 10

    return precio

def main():

    otra = "S"
    total = 0
    cont_queso = 0

    while (otra == "S"):

        print("Tipo de Hamburguesa (C, P)" )
        tipo = input()
        print("Con queso? (S, N)" )
        queso = input()

        if queso == "S":
            cont_queso = cont_queso + 1

        pre_ham = precio_hamb(tipo, queso)
        print(pre_ham)

        total = total + pre_ham

        print("Otra hamburguesa? (S, N)" )
        otra = input()
    print(f"Total de dinero del dia {total}" )
    print(f"Cantidad de hamburguesas con queso {cont_queso}")

main()