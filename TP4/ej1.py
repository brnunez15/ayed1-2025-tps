def es_capicua(cadena: str) -> bool:
    """
    Define si una cadena de caracteres es capicua.

    Pre: 
        cadena: recibe la cadena de caracteres y para agregarlos a una lista.

    Post:
        True: si la lista con la cadena de caracteres es capicua.
        False: si la lista con la cadena de caracteres no es capicua
    """
    lista = [elem for elem in cadena]
    lista_inversa = lista.copy()
    lista_inversa.reverse()
    return lista == lista_inversa

def main() -> None:
    c = input("Ingrese una cadena de caracteres: ")
    capicua = es_capicua(c)
    if capicua:
        print(f"La cadena ingresada: '{c}', es capicua")
    else:
        print(f"La cadena ingresada: '{c}', no es capicua")

if __name__ == "__main__":
    main()