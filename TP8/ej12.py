from typing import Dict, Tuple

def crear_libreria(claves: list[int], valores: list[int]) -> Dict:
    """
    Crea un diccionario.
    
    Pre:
        - claves: es una lista con los isbn ingresados por el usuario, las cuales seran las futuras claves del diccionario.
        - valores: es una lista con los precios de los libros, los cuales seran los valores del diccionario.

    Post:
        - retorna el diccionario creado.
    """
    return dict(zip(claves, valores))

def mostrar_libreria(libreria: dict) -> None:
    """
    Imprime en pantalla un diccionario recibido.

    Pre:
        - libreria: recibe el diccionario a imprimir.
    """
    for isbn, precio in libreria.items():
        print(f"ISBN: {isbn}: ${precio:.2f}")

def incrementar_precios(libreria: dict) -> Dict:
    """
    Incrementa todos los precios de los libros un 15%.

    Pre:
        - libreria: recibe el diccionario que se usara para obtener los valores (precios).
    
    Post:
        - libreria_incrementada: devuelve un nuevo diccionario con los valores modificados.
    """
    libreria_incrementada = {}
    for isbn, precio in libreria.items():
        nuevo_precio = precio + precio * 0.15
        libreria_incrementada[isbn] = nuevo_precio
    return libreria_incrementada

def buscar_mayor(libreria: dict) -> Tuple[int, int]:
    """
    Busca el libro con el precio mayor de un diccionario.

    Pre:
        - libreria: diccionario donde la clave es el ISBN (int) y el valor es el precio (int).
    
    Post:
        - isbn_mayor: entero, clave del libro con el precio mas alto.
        - libreria[isbn_mayor]: entero, precio del libro mas caro.
    """
    isbn_mayor = max(libreria, key=libreria.get)
    return isbn_mayor, libreria[isbn_mayor]

def main() -> None:
    """
    Funcion principal del programa.
    """
    lista_isbn = []
    lista_precios = []
    while True:
        try:
            isbn = int(input("Ingrese el ISBN del libro (-1 para salir): "))
            if isbn == -1:
                print()
                break
            precio = int(input(f"Ingrese el precio del libro {isbn}: "))
            lista_isbn.append(isbn)
            lista_precios.append(precio)

        except ValueError:
            print("\nEl numero debe ser un numero entero valido.\n")

    if lista_isbn:
        print("\n----LISTADO DE LIBROS----\n")
        libreria = crear_libreria(lista_isbn, lista_precios)
        mostrar_libreria(libreria)
        print("\n----LISTADO DE LIBROS + 15%----\n")
        libreria_incrementada = incrementar_precios(libreria)
        mostrar_libreria(libreria_incrementada)

        isbn_mayor, precio_mayor = buscar_mayor(libreria_incrementada)
        print(f"\nEl libro con el precio mayor es ISBN: {isbn_mayor}: ${precio_mayor:.2f}")
    else:
        print("No hay libros ingresados.")

if __name__ == "__main__":
    main()