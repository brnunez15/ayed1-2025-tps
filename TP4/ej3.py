from typing import List, Tuple

def separar_claves(cm: str) -> Tuple[List[str], List[str]]:
    """
    Separa los elementos de un string en dos listas dependiendo sus posiciones.
    La primer lista se guardan los elementos con numero de posicion par.
    La segunda lista se guaran los elementos con numero de posicion impar.

    Pre:
        cm: recibe la clave maestra que es la clave "intercalada".

    Post:
        c1, c2: devuelve una tupla de dos listas con las claves separadas (strings) de la clave maestra.
    """
    c1 = [c for i, c in enumerate (cm) if i % 2 == 0 ]
    c2 =  [c for i, c in enumerate (cm) if i % 2 != 0 ]
    return c1,c2

def main() -> None:
    clave_maestra = input("Ingrese la clave maestra: ")
    clave1, clave2 = separar_claves(clave_maestra)

    print(f"La clave 1 es: {''.join(clave1)}")
    print(f"La clave 2 es: {''.join(clave2)}")

if __name__ == "__main__":
    main()