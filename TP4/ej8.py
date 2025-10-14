def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Guarda los ultimos n caracteres de una cadena en una subcadena.

    Pre:
        - cadena: cadena de caracteres original, a modificar.
        - n: entero que representa la cantidad de los ultimos caracateres de la cadena.

    Post:
        - subcadena: cadena de caracetres con los ultimos n caracteres de la cadena original.
    """
    subcadena = cadena[-n:]
    return subcadena

def main() -> None:
    c = input("Ingrese una cadena de caracteres: ")
    try:
        n = int(input("Ingrese la cantidad de los ultimos caracteres que desea que se impriman: "))

        if n <= len(c):
            cadena = ultimos_caracteres(c,n)
            print(cadena)
        else:
            print("El numero de caracteres debe ser correspondiente a la cantidad de caracteres de la cadena ingresada.")

    except ValueError:
        print("Debe ingresar un numero entero valido.")

if __name__ == "__main__":
    main()