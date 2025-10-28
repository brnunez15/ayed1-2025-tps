from typing import Dict

def contar_vocales(palabra: str) -> Dict:
    """
    Cuenta cuantas vocales tiene una palabra.

    Pre:
        - palabra: recibe un string con la palabra a analizar.
    
    Post:
        - vocales: devuelve un diccionario con todas las vocales y cuantas veces aparecio una vocal en la palabra.
    """
    vocales = {v : 0 for v in "aeiou"}
    palabra = palabra.lower()
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1
    return vocales

def main() -> None:
    """
    Funcion principal del programa.
    """
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    
    print("\n----CANTIDAD DE VOCALES ENCONTRADAS----\n")
    for palabra in palabras:
        contar = contar_vocales(palabra)
        print(f"{palabra} -> {contar}")

if __name__ == "__main__":
    main()