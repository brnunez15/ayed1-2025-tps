def esta_ordenada_ascendente(lista: list[int]) -> bool:
    """
    Verifica si una lista esta ordenada de manera ascendente.

    Pre: Recibe una lista de numeros enteros para realizar la verificacion.

    Post: Devuelve True si la lista esta ordenada de forma ascendente. O False en su contrario.
    """
    return lista == sorted(lista)

def main () -> None:
    lista_ascendente = [1, 2, 3]
    lista_descendente = ['b', 'a']

    esta_ordenada = esta_ordenada_ascendente(lista_descendente)

    if esta_ordenada:
        print(f"La lista esta ordenada de forma ascendente")
    else:
        print(f"La lista esta ordenada de forma descendente")

if __name__ == "__main__":
    main()