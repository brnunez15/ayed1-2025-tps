import random as rn
from typing import Dict,List

def gen_num() -> int:
    """
    Genera un numero aleatorio entre 1 y 50.

    Post:
        - devuelve el numero generado.
    """
    return rn.randint(1,50)

def generar_diccionario() -> Dict:
    """
    Genera un diccionario.
    - Clave: genera claves del 1 al 10.
    - Valor: genera numeros aleatorioes entre 1 y 50.

    Post:
        - devuelve el diccionario generado.
    """
    return {i: gen_num() for i in range(1, 11)}

def buscar_clave(diccionario: dict, valor: int) -> List[int]:
    """
    Busca la o las claves con el valor que coincidan con el recibido.

    Pre:
        - diccionario: diccionario recibido donde se realizara la comparacion de valores.
        - valor: entero, que representa el valor para buscar sus claves coincidentes.

    Post:
        - lista: lista de enteros donde se guardaran las claves que coincidieron con los valores.
        Si no coincide ninguna, devuelve una lista vacia.
    """
    lista = []
    for c, v in diccionario.items():
        if v == valor:
            lista.append(c)
    return lista

def mostrar_diccionario(diccionario: dict) -> None:
    """
    Imprime un diccionario.

    Pre:
        - diccionario: recibe el diccionario que se quiere imprimir.
    """
    for clave, valor in diccionario.items():
        print(f"{clave} : {valor}")

def main() -> None:
    """
    Funcion principal del programa.
    """
    d = generar_diccionario()
    mostrar_diccionario(d)
    while True:
        try:
            valor = int(input("\nIngrese un valor: "))

            buscar = buscar_clave(d, valor)

            if buscar:
                print(f"\nLas claves del diccionario con valor {valor} son: {buscar}")
            else:
                print(f"\nNo se encontro una clave con el valor: {valor}")
            break
        except ValueError:
            print("ERROR. Debe ingresar un numero entero valido")

if __name__ == "__main__":
    main()