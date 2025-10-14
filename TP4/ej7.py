# def eliminar_cadena(cadena: str, posicion: int, characteres: int) -> str:
#     """
#     Elimina una cantidad determinada de caracteres de una cadena,
#     comenzando desde una posición específica.

#     Pre:
#         - cadena: cadena de caracteres a modificar.
#         - posicion: entero que representa la podicion desde donde se comenzara a eliminar.
#         - characteres: cantidad de caracteres que se eliminaran a partir de la posicion recibida.

#     Post:
#         - Devuelve una nueva cadena sin el rango de caracteres eliminado.
#     """
#     subcadena = ""
#     for i, caracter in enumerate (cadena):
#         if i < posicion or i >= posicion + characteres:
#             subcadena += caracter
#     return subcadena

def eliminar_cadena(cadena: str, posicion: int, characteres: int) -> str:
    """
        Elimina una cantidad determinada de caracteres de una cadena,
        comenzando desde una posición especifica.

    Pre:
        - cadena: cadena de caracteres a modificar.
        - posicion: entero que representa la podicion desde donde se comenzara a eliminar.
        - characteres: cantidad de caracteres que se eliminaran a partir de la posicion recibida.

    Post:
        - Devuelve una nueva cadena formada por la concatenacion de los fragmentos
          antes y despues del rango eliminado.
    """
    subcadena1 = cadena[: posicion]
    subcadena2 = cadena[posicion + characteres:]
    return subcadena1 + subcadena2

def main():
    c = input("Ingresa una frase: ")
    try:
        p = int(input("Ingrese una posicion: "))
        ch = int(input("Ingrese una cantidad de caracteres a eliminar: "))

        if p >= 0 and p + ch <= len(c):
            eliminar = eliminar_cadena(c,p,ch)
            print(eliminar)
        else:
            print("Debe ingresar una posicion o una cantidad de caracteres validos.")

    except ValueError:
        print("Debe ingresar un numero entero valido.")
        
if __name__ == "__main__":
    main()