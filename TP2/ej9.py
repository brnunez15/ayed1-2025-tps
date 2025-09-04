from typing import List

def generar_lista(a: int, b: int) -> List[int]:
    """
    Genera una lista de numeros enteros que sean multiplos de 7 pero no multiplos de 5.

    Pre: Recibe dos datos enteros que representan el rango de la cantidad de elementos de la lista.

    Post: Devuelve la lista de enteros.
    """
    return [x for x in range (a, b + 1) if x % 7 == 0 and x % 5 != 0]

def main() -> None:
    a = int(input("Ingrese un numero desde: "))
    b = int(input("Ingrese un numero hasta: "))
    lista = generar_lista(a, b)
    print(lista)

if __name__ == "__main__":
    main()