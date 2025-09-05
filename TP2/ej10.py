import random as rn
from random import randint
from typing import List

def generar_lista() -> List[int]:
    """
    Genera una lista de numeros aleatorios enteros.

    Post: devuelve una lista de numeros enteros.
    """
    return [rn.randint(1, 100) for _ in range(20)]

def impares(lista: list[int]) -> List[int]:
    """
    Filtra los elementos de una lista los que son numeros impares y los agrega a una nueva lista.

    Pre: recibe la lista con los elementos originales.

    Post: devuelve una nueva lista con los datos filtrados de la lista original.
    """
    return list(filter(lambda x: x % 2 != 0, lista))

def main() -> None:
    lista = generar_lista()
    lista_impares = impares(lista)

    print(f"Lista original: {lista}")
    print(f"Misma lista filtrada por impares: {lista_impares}")

if __name__ == "__main__":
    main()