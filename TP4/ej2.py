def centrar_cadena(cadena: str) -> None:
    """
    Imprime una cadena de caracteres de manera centrada suponiendo que la pantalla contiene 80 columnas.

    Pre:
        cadena: cadena que se va a centrar.
    """
    espacios = (80 - len(cadena) // 2)
    print(" " * espacios + cadena)

def main() -> None:
    c = input("Ingresar texto: ")
    centrar_cadena(c)

if __name__ == "__main__":
    main()