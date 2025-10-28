from typing import Dict

def crear_diccionario() -> Dict:
    """
    Crea un diccionario con sus claves con numeros enteros del 1 al 20 y sus valores es el cuadrado de sus claves.

    Post:
        - diccionario: diccionario creado con sus claves y valores correspondientes.
    """
    diccionario = {i: i**2 for i in range(1, 21)}
    return diccionario

def main() -> None:
    """
    funcion principal del programa.
    """
    diccionario = crear_diccionario()
    for clave, valor in diccionario.items():
        print(f"{clave}:{valor}")

if __name__ == "__main__":
    main()