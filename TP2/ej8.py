from typing import List

def generar_lista_impares() -> List[int]:
    """
    Genera una lista de numeros enteros impares.

    Post: devuelve la lista de enteros impares.
    """
    return ([x for x in range(100, 201) if x % 2 != 0])

def main() -> None:
    lista = generar_lista_impares()
    print(lista)

if __name__ == "__main__":
    main()