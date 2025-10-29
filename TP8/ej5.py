def es_ortogonal(comp1: tuple[int, int], comp2: tuple[int,int]) -> bool:
    """
    Verifica si dos componentes son ortogonales o no.

    Pre:
        recibe 2 tuplas.
        - comp1: primer componente que contiene el valor de x y el valor de y.
        - comp2: segundo componente que contiene el valor de x y el valor de y.
    
    Post:
        - True: devuelve True si los componentes son ortogonales.
        - False: devuelve False en caso contrario.
    """
    x1, y1 = comp1
    x2, y2 = comp2
    return (x1 * x2) + (y1 * y2) == 0

def main() -> None:
    """
    Funcion principal del programa.
    """
    while True:
        try:
            print("\n--VALORES DEL PUNTO A--\n")
            x1 = int(input("Ingrese el valor de x: "))
            y1 = int(input("Ingrese el valor de y: "))

            print("\n--VALORES DEL PUNTO B--\n")
            x2 = int(input("Ingrese el valor de x: "))
            y2 = int(input("Ingrese el valor de y: "))

            ortogonal = es_ortogonal((x1,y1), (x2, y2))
            if ortogonal:
                print("\nLos componentes ingresados son ortogonales!")
            else:
                print("\nLos componentes ingresados no son ortogonales.")
            break
        except ValueError:
            print("\nERROR. Debe ingresar un numero entero valido.")

if __name__ == "__main__":
    main()