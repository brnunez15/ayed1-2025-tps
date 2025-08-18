def concatenar_numeros (n1: int, n2: int) -> str:
    """
    Concatena dos números enteros

    Pre: los números tienen que ser enteros positivos.

    Post: Devuelve los dos números concatenados, siendo previamente casteados a string.
    """
    
    return str(n1) + str(n2)

def main () -> None:
    """
    Funcion principal del programa.
    """
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    if n1 > 0 and n2 > 0:
        print(concatenar_numeros(n1, n2))
    else:
        print("Los numeros deben ser positivos")

if __name__ == "__main__":
    main()