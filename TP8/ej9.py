from typing import Dict

def generar_tabla(n: int) -> Dict:
    """
    Genera una diccionario con las claves del 1 al 13. Y su valor es el producto de n y su clave.

    Pre:
        - n: numero entero ingresado por el usuario el cual se va a multiplicar por una clave y va a ser el futuro valor de la misma.
    
    Post:
        - retorna el diccionario generado.
    """
    return {i: i * n for i in range(1, 13)}

def mostrar_tabla(n: int, tabla: dict) -> None:
    """
    Imprime el diccionario en forma de tabla.

    Pre:
        - n: numero que ingreso el usuario que representa la tabla que desea saber.
        - tabla: diccionario generado previamente.
    """
    print(f"\n----TABLA DEL {n}----\n")
    for clave, valor in tabla.items():
        print(f"{n} x {clave} = {valor}")

def main() -> None:
    """
    Funcion principal del programa.
    """
    while True:
        try:
            n = int(input("Ingresa la tabla que deseas saber: "))
            tabla = generar_tabla(n)
            mostrar_tabla(n, tabla)
            break
        except ValueError:
            print("\nERROR. Debe ingresar un numero entero valido.\n")

if __name__ == "__main__":
    main()