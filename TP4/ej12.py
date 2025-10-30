from typing import List, Tuple

def gen_numeros() -> List[str]:
    """
    Genera una lista con strings numericos del 1 al 12.

    Post:
        Devuelve la lista con los strings creados.
    """
    return [str(i) for i in range(1,13)]

def gen_palos() -> Tuple[str]:
    """
    Genera una tupla con str representando los palos de los naipes.

    Post:
        - devuelve la tupla creada de strings (palos)
    """
    return ("Oro", "Copa", "Basto", "Espada")

def crear_naipes(numeros: list[str], palos: tuple[str]) -> List[str]:
    """
    Crea una lista con strings, representando todas las cartas de la baraja española.

    Pre:
        - Recibe una lista con los numeros correspondientes a un juego de cartas(1,12) casteados a str.
        - recibe una tupla de strings con los nombres de los palos de los naipes.
    
    Post:
        Devuelve la lista con todas las cartas con su palo correspondiente.
    """
    return [f"{numero} de {palo}" for numero in numeros for palo in palos]

def main()-> None:
    """
    Funcion principal del programa.
    """
    numeros = gen_numeros()
    palos = gen_palos()
    naipes = crear_naipes(numeros, palos)
    print("\n----NAIPES DE LA BARAJA ESPAÑOLA----\n")
    print(naipes)

if __name__ == "__main__":
    main()