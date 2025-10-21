from typing import Tuple

def reemplazar(cadena: str, palabra_cambio: str, palabra_original: str) -> Tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra por otra recibida, en una cadena de caracteres.

    Pre:
        - cadena: cadena de caracteres original, donde se buscaran las palabras a cambiar.
        - palabra_cambio: str ingresado por el usuario la cual va a ser la nueva palabra a cambiar.
        - palabra_original: str ingresado por el usuario la cual represena la palabra que el usuario desea cambiar de la cadena original.
    
    Post:
        TUPLA
        - c: cadena de caracteres con sus palabras reemplazadas.
        - contador: entero que representa la cantidad de veces que se realizo un cambio en la cadena.
    """
    c = cadena.split()
    contador = 0
    for i, p in enumerate(c):
        if p == palabra_original:
            c[i] = palabra_cambio
            contador += 1
    c = " ".join(c)
    return c, contador

def main() -> None:
    """
    Funcion principal del programa.
    """
    cadena = input("Ingrese una cadena de caracteres: ")
    print(f"\n{cadena}\n")

    original = input("¿Que palabra desea cambiar?: ")
    cambio = input("¿Por que palabra la deseas cambiar?: ")

    reemplazo, veces = reemplazar(cadena, cambio, original)
    print(f"\nCadena reemplazada: {reemplazo}\n")
    print(f"La palabra '{cambio}' se cambio {veces} veces")

if __name__ == "__main__":
    main()