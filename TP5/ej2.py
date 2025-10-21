def sumar_cadenas(cadena1: str, cadena2: str) -> int:
    """
    Suma dos cadenas.
    
    Pre:
        - cadena1: primer cadena ingresada por el usuario que deben ser caracteres numericos.
        - cadena2: segunda cadena ingresada por el usuario que deben ser caracteres numericos.
    
    Post:
        - castea las dos cadenas a enteros y devuelve la suma de los dos numeros.
    """
    return int(cadena1) + int(cadena2)

def main() -> None:
    try:
        c1 = input("Ingrese un numero: ")
        c2 = input("Ingrese un numero: ")

        suma = sumar_cadenas(c1, c2)

        print(f"La suma entre los dos numeros es: {suma}")

    except ValueError:
        print("Debe ingresar un numero entero valido para realizar la suma.")

if __name__ == "__main__":
    main()