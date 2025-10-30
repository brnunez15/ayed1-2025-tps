def contar_subcadena(cadena: str, subcadena: str) -> int:
    """
    Cuenta las veces que encuentra la subcadena completa en la cadena recibida.

    Pre:
        - cadena: recibe un string de la frase/texto/palabra ingresada por el usuario.
        - subcadena: recibe un string de la subcadena que se buscara dentro de la cadena original.

    Post:
        - contador: devuelve un int representando las veces que la subcadena aparecio en la cadena original.
    """
    cadena = cadena.lower()
    subcadena = subcadena.lower()
    contador = 0
    i_subcadena = 0
    for caracter in cadena:
        if caracter == subcadena[i_subcadena]:
            i_subcadena += 1
            if i_subcadena == len(subcadena):
                contador += 1
                i_subcadena = 0
    return contador

def main() -> None:
    """
    Funcion principal del programa.
    """
    c = input("Ingrese una cadena: ")
    s = input("Ingrese una subcadena: ")
    contar = contar_subcadena(c,s)
    print(f"La cantidad de apariciones de la subcadena: {s}, fueron {contar} veces")

if __name__ == "__main__":
    main() 