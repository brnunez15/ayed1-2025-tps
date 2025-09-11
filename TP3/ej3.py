import random as rn
from random import randint
from typing import List

def generar_matriz (n: int) -> List[list[int]]:
    """
    Genera una matriz con numeros aleatorios sin repetidos.

    Pre: Recibe el numero de la cantidad de filas y columnas.

    Post: Devuelve la matriz generada con sus respectivas condiciones.
    """
    return [list(set([rn.randint (0, n**2 - 1) for _ in range(n)]))for _ in range(n)]

def main() -> None:
    n = int(input("Ingrese un numero para la cantidad de filas y columnas: "))
    matriz = generar_matriz(n)
    print(matriz)

if __name__ == "__main__":
    main()