import random as rn
from random import randint
from typing import List

def generar_lista() -> List[int]:
    """
    Genera una lista de 5 numeros enteros aleatorios.

    Post: Retorna la lista de enteros.
    """
    return [rn.randint(1,10) for _ in range (rn.randint(1,5))]

def intercalar_listas(lista1: list[int], lista2: list[int]) -> List[int]:
    """
    Intercala elementos entre dos listas de enteros.

    Pre: recibe una primer lista a la que se le intercalaran los elementos de la 2da lista recibida.

    Post: Devuelve la primer lista con los elementos de la 2da lista intercalados.
    """   
    for y, dato in enumerate(lista2):
        x = 2 * y + 1
        lista1[x:x] = [dato]
    
    return lista1

def main() -> None:
    lista_1 = generar_lista()
    lista_2 = generar_lista()
    print(f"Lista 1: {lista_1}")
    print(f"Lista 2: {lista_2}")

    intercalar = intercalar_listas(lista_1, lista_2)
    print(f"Listas intercaladas: {intercalar}")

if __name__ == "__main__":
    main()