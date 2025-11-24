def cantidad_digitos(numero: int) -> int:
    """
    Cuenta la cantidad de digitos que tiene un número entero realizando una division entera por 10, restando asi su ultimo digito.

    Pre:
        - numero: entero que recibe para calcular.

    Post:
        - devuelve un entero que representa la cantidad de digitos que tiene "numero".
    """
    if numero < 10:
        return 1
    return 1 + cantidad_digitos(numero // 10)

def main() -> None:
    """
    Funcion principal del programa.
    """
    while True:
        try:
            n = int(input("Ingrese un número: "))
            cant_dig = cantidad_digitos(n)
            print(f"El número {n} tiene {cant_dig} dígitos.")
            break
        except ValueError:
            print("\nERROR. Debe ingresar un número entero.\n")

if __name__ == "__main__":
    main()