from typing import List

def generar_lista(n: int) -> List[int]:
    """
    Genera una lista de numeros enteros con sus cuadrados.

    Pre: Recibe la cantidad de elementos de la lista.

    Post devuelve una lista de numeros enteros son sus respectivos cuadrados.
    """
    return [(i + 1) ** 2 for i in range(n)]

def main() -> None:
    numero = int(input("Ingrese un numero: "))
    lista = generar_lista(numero)
    print(lista)

    print(f"Ultimos 10 valores de la lista: {lista[10:]}")

if __name__ == "__main__":
    main()