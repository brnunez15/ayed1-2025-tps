from typing import List

def buscar_mayor(lista: List[int]) -> int:
    """
    Busca el numero mayor de una lista con elementos de números enteros.

    Pre: La lista no debe estar vacia.

    Post: Devuelve el número mayor solo si este es unico. Sino devuelve -1.
    """

    if len(lista) > 0:

        mayor = max(lista)
        contador = 0

        for i in lista:
            if i == mayor:
                contador += 1
        
        if contador != 1:
            return -1
        
        return mayor

def ingresar_numeros() -> int:
    """
    Le pide al usuario que ingrese números enteros.

    Post: Devuelve un número entero ingresado por el usuario.
    """
    num = int(input("Ingresa un numero: "))
    return num

def agregar_numeros() -> List[int]:
    """
    Agrega números enteros a una lista.

    Post: Devuelve una lista cargada de números que fueron ingresados por un usuario.
    """
    numeros = list()
    for _ in range (3):
        numero = ingresar_numeros()
        numeros.append(numero)
    return numeros

def main() -> None:
    """
    Función principal del programa.
    """
    numeros = agregar_numeros()
    print(f"El numero mayor es: {buscar_mayor(numeros)}")
    return None

if __name__ == "__main__":
    main()