def crear_set() -> set:
    """
    crea un conjunto con numeros del 0 al 9.

    Post:
        - conjunto: set con los numeros cargados.
    """
    conjunto = set()
    for i in range(10):
        conjunto.add(i)
    return conjunto

def eliminar_numero(numero: int, numeros: set) -> set:
    """
    Elimina un numero del conjunto.

    Pre:
        - numero: recibe el numero a eliminar.
        - numeros: recibe el conjunto donde se encuentran los numeros candidatos para eliminar.
    """
    numeros.remove(numero)
        
def main() -> None:
    """
    Funcion principal del programa.
    """
    conjunto = crear_set()
    print(conjunto)
    while True:
        try:
            n = int(input("Ingrese un numero entre 0-9: "))
            if n == -1:
                print("Saliendo...")
                break
            eliminar_numero(n, conjunto)
            print(f"\n{conjunto}\n")

        except ValueError:
            print("\nERROR. Debe ser un numero entero\n")
            print(f"\n{conjunto}")
        except KeyError:
            print("\nERROR. Debe ingresar un numero que este dentro del conjunto.\n")
            print(f"\n{conjunto}")

    print(f"\nConjunto con valores eliminados: {conjunto}\n")

if __name__ == "__main__":
    main()