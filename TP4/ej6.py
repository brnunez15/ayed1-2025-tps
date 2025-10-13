from typing import Tuple
#sin rebanadas
"""
def extraer_cadena(cadena: str, posicion: int) -> Tuple[str, int]:
    subcadena = ""
    caracteres = 0
    for i, caracter in enumerate(cadena):
        if i >= posicion:
            subcadena += caracter
            caracteres += 1
    return subcadena, caracteres
"""
#con rebanadas
def extraer_cadena(cadena: str, posicion: int) -> Tuple[str, int]:
    """
    Extrae una subcadena partiendo desde una posicion de la cadena original.

    Pre:
        - cadena: cadena original.
        - posicion: entero ingresado por el usuario, representando la posicion de partida.
    
    Post:
        TUPLA:
        - subcadena: cadena extraida de la original con los elementos que se encuentran a partir de la posicion recibida.
        - caracteres: entero que representa la cantidad de elementos que contiene la subcadena.
    """
    subcadena = cadena[posicion:]
    caracteres = len(subcadena)
    return subcadena, caracteres

def main() -> None:
    c = input("Ingresa una frase: ")
    try:
        p = int(input("Ingresa la posicion: "))
        if p <= len(c):
            subcadena, caracter = extraer_cadena(c, p)
            print(f"La subcadena {subcadena} comienza desde la posicion: {p} y tiene {caracter} caracteres")
        else:
            print("Debe ingresar una posicion valida.")
    except ValueError:
        print("Debe ingresar un numero entero.")

if __name__ == "__main__":
    main()