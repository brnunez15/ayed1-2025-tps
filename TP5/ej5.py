import math

def calcular_raiz(numero: int) -> float:
    """
    Calcula la raiz cuadrada de un numero.

    Pre:
        - numero: entero positivo que va a ser calculada su raiz.
    
    Post:
        - flotante que representa el resultado a la raiz cuadrada del numero recibido.
    """
    return math.sqrt(numero)

def main() -> None:
    """
    Funcion principal del programa.
    """
    try:
        n = int(input("Ingresa un numero: "))
        raiz = calcular_raiz(n)
        print(raiz)
    except ValueError:
        print("El numero debe ser entero positivo.")

if __name__ == "__main__":
    main()