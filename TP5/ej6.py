from typing import List

def cargar_lista() -> List[int]:
    """
    Carga una lista con numeros enteros ingresados por el usuario hasta ingresar -1.

    Post:
        -lista: devuelve la lista con los numeros cargados.
    """
    lista = []
    while True:
        try:
            numero = int(input("Ingresa un numero: "))
            if numero == -1:
                break
            lista.append(numero)
        except ValueError:
            print("Debe ingresar un numero.")
    return lista

def buscar_indice(numero: int, lista: list[int]) -> int:
    """
    Busca el indice de un elemento de una lista.

    Pre:
        - numero: recibe un entero ingresado por el usuario, representando un elemento de la lista.
        - lista: lista la cual se buscara el indice del elemento recibido.
    
    Post:
        - devuelve el indice del elemento de la lista.
    """
    return lista.index(numero)

def main() -> None:
    """
    Funcion principal del programa. 
    No pueden haber mas de 3 errores al intento de ingresar el elemento de la lista.
    """
    lista = cargar_lista()
    print(f"Lista cargada: {lista}")
    errores = 0

    while True:
        try:
            n = int(input("Ingrese un numero de la lista, -1 para salir: "))
            if n == -1:
                print("Saliendo...")
                break
            try:
                indice = buscar_indice(n, lista)
                print(f"El indice del numero {n} es: {indice}")
            except ValueError:
                errores += 1
                print("El numero no esta ingresado en la lista.")
                if errores == 3:
                    print(f"Ocurrieron {errores} errores.")
                    break
        except ValueError:
            print("Debe ingresar un numero entero.")

if __name__ == "__main__":
    main()