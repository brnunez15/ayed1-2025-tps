import random as rn
from random import randint
from typing import List

def generar_lista() -> List[int]:
    """
    Crea una lisa de numeros enteros.

    Post: devuelve una lista con 10 elementos.
    """
    return [i for i in range(1, 11)]

def segunda_lista() -> List[int]:
    """
    Crea una lista de numeros enteros.

    Post: Devuelve una lista de 10 numeros aleatorios sin repetirse, del 1 al 10.
        Si se repiten, no se imprimen.
    """
    return list(set([rn.randint(1, 10) for i in range(1, 11)]))

def eliminar_valores(lista1: list[int], lista2: list[int]) -> List[int]:
    """
    Elimina los valores que coinciden de otra lista, a la lista original.

    Pre: recibe dos listas: la original y la que contiene los numeros a eliminar.

    Post: Devuelve la lista original con sus valores eliminados.
    """
    for num in lista2:
        while num in lista1:
            lista1.remove(num)
    return lista1


def main() -> None:
    lista = generar_lista()
    lista_2 = segunda_lista()
    print(f"Lista original: {lista}")
    print(f"Lista de valores a eliminar: {lista_2}")

    lista_resultante = eliminar_valores(lista, lista_2)
    print(f"Lista resultante: {lista_resultante}")

if __name__ == "__main__":
    main()