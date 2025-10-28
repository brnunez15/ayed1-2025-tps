def validar_encaje(ficha1: tuple[int, int], ficha2: tuple[int, int]) -> bool:
    """
    Valida si dos fichas(tuplas) encajan. Es decir, coinciden con algun numero.

    Pre:
        - ficha1: tupla de dos enteros a comparar.
        - ficha2: tupla de dos enteros a comparar.
    
    Post: 
        - encaja: booleano
        - True: si las dos fichas (tuplas) coinciden con algun numero en comun.
        - False: en caso contrario.
    """
    encaja = False
    f1 = set(ficha1)
    f2 = set(ficha2)
    for n in f1:
        if n in f2:
            encaja = True
    return encaja

def main() -> None:
    """
    Funcion principal del programa.
    """
    f1 = (3, 6)
    f2 = (5, 6)
    validar = validar_encaje(f1, f2)
    if validar:
        print(f"Las fichas {f1} y {f2} encajan!")
    else:
        print(f"Las fichas {f1} y {f2} no encajan.")

if __name__ == "__main__":
    main()