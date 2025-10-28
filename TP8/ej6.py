def eliminar_repetidos(frase: str) -> set:
    """
    Crea un nuevo string eliminando las puntuaciones y las palabras repetidas.

    Pre:
        - frase: string ingresada por el usuario la cual sera modificada.

    Post:
        - conjunto de la nueva frase, sin repetidos.
    """
    puntuacion = [".", ",", ";", ":", "!", "?", "¿", "¡"]
    frase = frase.lower()
    frase_nueva = ""

    for ch in frase:
        if ch not in puntuacion:
            frase_nueva += ch  

    palabras = frase_nueva.split()
    return set(palabras)

def ordenar_frase(sin_repe: set) -> str:
    """
    Ordena la frase sin palabras repetidas.

    Pre:
        - sin_repe: conjunto de la frase con palabras sin repetir.

    Post:
        - retorna un string con las palabras ordenadas segun su longitud y alfabeticamente.
    """
    lista_ordenada = sorted(sin_repe, key=len)
    return " ".join(lista_ordenada)

def main() -> None:
    """
    Funcion principal del programa.
    """
    f = input("Ingrese una frase: ")
    sin_repetidos = eliminar_repetidos(f)
    frase_ordenada = ordenar_frase(sin_repetidos)

    print(f"La frase sin palabras repetidas ni puntuaciones: {" ".join(sin_repetidos)}")
    print(f"La frase sin repetidos y ordenada: {frase_ordenada}")

if __name__ == "__main__":
    main()