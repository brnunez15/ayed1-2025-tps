import random as rn
from typing import Dict, Tuple
rn.seed(1)

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

def eliminar_claves(diccionario: dict, claves: list[int]) -> Tuple[dict, list[int], int]:
    """
    Elimina claves de un diccionario, si estas existen. Si no existen se agregan a una lista.

    Pre:
        - diccionario: recibe el diccionario con las claves y valores a eliminar.
        - claves: lista con las claves ingresadas por el usuario, a eliminar.
    
    Post:
        TUPLA
        - diccionario: diccionario con sus claves eliminadas.
        - claves_otras: lista con las claves que no existen en el diccionario recibido.
        - veces: entero de las veces que se elimino una clave del diccionario.
    """
    claves_otras = []
    veces = 0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            veces += 1
        else:
            claves_otras.append(clave)
    return diccionario, claves_otras, veces

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
    Funcion principal.
    """
    diccionario = generar_diccionario()
    mostrar_diccionario(diccionario)

    claves = []
    while True:
        try:
            clave = int(input("Ingrese la clave que deseas eliminar (-1 para salir): "))
            if clave == -1:
                break
            claves.append(clave)
        except ValueError:
            print("\nERROR. Debe ingresar un numero entero valido.\n")

    eliminar, otras, veces = eliminar_claves(diccionario, claves)
    mostrar_diccionario(eliminar)

    if veces:
        print(f"Cantidad de claves eliminadas: {veces}")
    if otras:
        print(f"Las claves ingresadas: {otras} no se encontraron en el diccionario.")

if __name__ == "__main__":
    main()