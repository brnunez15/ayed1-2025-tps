def sumar_naturales (numero: int) -> int:
    """
    Suma los primeros N naturales consecutivos.

    Pre:
        - numero: recibe el numero entero a calcular.
    
    Post:
        - devuelve la suma de todos los numeros consecutivos de "numero"
    """
    if numero == 0:
        return 0
    return numero + sumar_naturales(numero - 1)

def main() -> None:
    """
    Funcion principal del programa
    """
    while True:
        try:
            n = int(input("Ingrese un numero natural: "))
            try:
                suma = sumar_naturales(n)
                print(f"La suma de los primeros {n} numeros naturales es: {suma}")
                break
            except RecursionError as e:
                print(f"\nERROR: {e}. Ingrese un numero menor a 997\n")
        except ValueError:
            print("\nERROR. Debe ingresar un numero entero valido.\n")

if __name__ == "__main__":
    main()