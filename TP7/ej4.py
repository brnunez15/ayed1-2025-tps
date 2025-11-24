def multiplicar(multiplicando: int, multiplicador: int) -> int:
    """
    Realiza la multiplicacion de dos numeros enteros sumando al multiplicando a la cantidad del multiplicador.

    Pre:
        - multiplicando: recibe un entero que representa el numero a multiplicar.
        - multiplicador: recibe un entero que representa el numero multiplicador.

    Post:
        devuelve la suma del multiplicando por la cantidad de veces del multiplicador.
    """

    if multiplicador == 0:
        return 0

    return multiplicando + multiplicar(multiplicando, multiplicador - 1)

def main() -> None:
    """
    Funcion principal del programa.
    """
    while True:
        try:
            n1 = int(input("Ingrese el valor del multiplicando: "))
            n2 = int(input("Ingrese el valor del multiplicador: "))
            resultado = multiplicar(n1, n2)
            print(f"El resultado de {n1}X{n2} es: {resultado}")
            break

        except ValueError:
            print("\nERROR. Debe ingresar un numero entero valido.\n")

if __name__ == "__main__":
    main()