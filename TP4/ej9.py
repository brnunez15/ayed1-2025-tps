def ordenar_palabras(cadena: str) -> str:
    """
    Ordena todas las palabras de menor a mayor elementos de una cadena de caracteres.

    Pre: 
        - cadena: recibe la cadena de caracteres a ordenar.
    
    Post:
        - resultado: devuelve la cadena de caracteres con sus palabras ordenadas.
    """
    lista_palabras = cadena.split()
    lista_palabras.sort(key = len)
    resultado = " ".join(lista_palabras)
    return resultado

def main() -> None:
    c = input("Ingrese una cadena de carateres: ")
    ordenar = ordenar_palabras(c)
    print(f"Cadena original: {c}")
    print(f"Cadena ordenada: {ordenar}")

if __name__ == "__main__":
    main()