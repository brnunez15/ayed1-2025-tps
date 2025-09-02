import random as rn
from typing import List, Tuple
from random import randint

# Ejercicio "a" y "b":

def cargar_lista() -> List[int]:
    """
       Carga una lista con elementos al azar. 

       Post: devuelve una lista con numeros al azar de 4 digitos y 
       la cantidad de elementos tambien sera al azar con numeros de 2 digitos.
    """
    elementos = rn.randint(10, 99)
    return [rn.randint(1000, 9999) for _ in range (elementos)]

def calcular_producto(lista: list[int]) -> int:
    """
    Calcula el producto de todos los elementos de una lista.

    Pre: recibe una lista de numeros enteros.

    Post: Devuelve un entero representando el resultado del producto de los elementos.
    """
    producto = 1
    for num in lista:
        producto *= num
    return producto

#Ejercicio "c":

def eliminar_valor(lista: list[int], valor: int) -> Tuple[List[int], bool]:
    """
    Elimina un valor de una lista.

    Pre: Recibe una lista candidata de numeros enteros la cual se le eliminara un valor;
        Y a su vex recibe un valor entero a eliminar ingresado por el usuario.

    Post: Devuelve una tupla de una lista de numeros enteros sin el valor que se ingreso.
        y un booleano que determina si el valor esta o no, en la lista.
    """

    if valor in lista:
        lista.remove(valor)
        return lista, True
    
    else:
        return lista, False

#Ejercicio "d"

def es_capicua(lista: list[int]) -> bool:
    """
    Define si una lista es capicua, o no.

    Pre: Recibe una lista de numeros enteros. Puede ser capicua, o no.

    Post: devuelve un booleano de acuerdo a la condicion de retorno.
    """
    return lista[0] == lista[-1]

def main() -> None:
    lista = cargar_lista()
    lista_prueba = [50, 17, 91, 17, 50]
    print(f"La lista tiene {len(lista)} elementos")
    print(lista)

    producto = calcular_producto(lista)
    print(f"El producto de todos los numeros de la lista es de: {producto}")

    valor_a_eliminar = int(input("Ingrese un valor para eliminar de la lista: "))
    lista_eliminada, se_encontro = eliminar_valor(lista, valor_a_eliminar)

    lista_es_capicua = es_capicua(lista_prueba)
    
    if se_encontro:
        print(f"Lista eliminada: {lista_eliminada}\n")
        print(f"Ahora la lista tiene {len(lista)} elementos.")
    else:
        print(f"El valor: {valor_a_eliminar} no se ha encontrado en la lista.")

    if lista_es_capicua:
        print(f"La lista: {lista_prueba} es capicua.")
    else:
        print(f"La lista: {lista_prueba} no es capicua")

if __name__ == "__main__":
    main()