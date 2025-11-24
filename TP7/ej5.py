def calcular_resto(dividendo: int, divisor: int) -> int:
    """
    Calcula el resto de una división utilizando restas sucesivas.
    Resta el divisor del dividendo hasta que el dividendo sea menor que el divisor.
    Ese valor final es el resto.

    Pre:
        - dividendo: recibe un entero representando el numero a dividir.
        - divisor: recibe un entero representando el numero por el cual se divide.
    
    Post:
        - devuelve el resultado del dividendo, es decir, el resto de la division.
    """
    if dividendo < divisor:
        return dividendo

    return calcular_resto(dividendo - divisor, divisor)

def main() -> None:
    """
    Funcion principal del programa.
    """
    while True:
        try:
            n1 = int(input("Ingrese el valor del dividendo: "))
            n2 = int(input("Ingrese el valor del divisor: "))
            resultado = calcular_resto(n1, n2)
            print(f"El resultado del resto de {n1}/{n2} es: {resultado}")
            break

        except ValueError:
            print("\nERROR. Debe ingresar un numero entero valido.\n")

if __name__ == "__main__":
    main()