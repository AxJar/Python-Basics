def linea_caracteres(tam):
    for cont in range(tam):
        print("*",end = "")
    print()

def main():
    n = int(input())

    for renglones in range(n):
        linea_caracteres(n)

main()