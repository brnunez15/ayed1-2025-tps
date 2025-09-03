import random as rn
from random import randint
from typing import List

def generar_lista(n: int) -> List[int]:
    """
    Genera una lista con numeros enteros aleatorios.

    Pre: recibe un numero entero por el usuario (representando la cantidad de elementos de la lista)

    Post: Devuelve una lista de numeros enteros aleatorios del 1 al 100.
    """
    return [rn.randint(1,100) for _ in range (n)]

def tiene_repetidos(lista: list[int]) -> bool:
    """
    Comprueba si una lista tiene elementos repetidos.

    Pre: recibe una lista de numeros enteros.

    Post: Devuelve un booleano (True) si contiene repetidos, (False) si no los tiene.
    """
    return len(lista) != len(set(lista))

def lista_elementos_unicos(lista: list[int]) -> List[int]:
    """
    Devuelve una lista sin elementos repetidos.

    Pre: recibe una lista con numeros enteros. (Puede ser con numeros repetidos, o no).

    Post: Devuelve una nueva lista pero sin los elementos repetidos. 
    El orden de los elementos puede no coincidir con la lista original.
    """
    return list(set(lista))

def main() -> None:
    numero = int(input("Ingrese un numero: "))
    lista = generar_lista(numero)
    print(lista)

    contiene_repetidos = tiene_repetidos(lista)
    elementos_unicos = lista_elementos_unicos(lista)

    if contiene_repetidos:
        print(f"La lista contiene repetidos.")
    else:
        print(f"La lista no contiene repetidos.")

    print(f"Lista sin elementos repetidos: {elementos_unicos}")

if __name__ == "__main__":
    main()