def main():
    print("Teclee n")
    n = int(input())

    suma = 0
    for valor in range(1, n+1):
        suma = suma + valor
        if valor < n:
            print(valor,end =" + ")
        else:
            print(valor, end = " = ")
    print(suma)

main()
