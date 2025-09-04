import random as rn
from random import randint
from typing import List

def generar_lista () -> List[int]:
    """
    Genera una lista de numeros enteros.

    Post: devuelve una lista con numeros enteros generados aleatoriamiente.
    """
    return [rn.randint(1, 10) for _ in range (3)]

def normalizar (lista: list[int]) -> List[float]:
    """
    Normaliza los elementos de una lista.

    Pre: Recibe una lista de numeros enteros. La cual sus elementos van a ser normalizados.

    Post: Devuelve una lista de flotantes, con cada elemento normalizado.
    """
    suma = sum(lista)
    lista_normalizada = list()

    for num in lista:
        resultado = num / suma
        lista_normalizada.append(resultado)
    
    return lista_normalizada

def main() -> None:
    lista = generar_lista()
    normalizada = normalizar(lista)
    print(f"Lista original: {lista}")
    print(f"Lista normalizada: {[round(num, 2) for num in normalizada]}")

if __name__ == "__main__":
    main()