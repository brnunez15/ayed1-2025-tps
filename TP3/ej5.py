import os
import random as rn
from random import randint
from typing import Lista, Tuple

def salir() -> None:
    """Insiste hasta que el usuario ingrese 0 para volver al menú."""
    while True:
        salir = input("\nIngrese 0 para volver al menú: ")
        if salir == "0":
            print("\nVolviendo al menú...\n")
            break
        else:
            print("\nDebe ingresar 0 para salir.\n")

def limpiar_pantalla() -> None:
    """
    Funcion para limpiar pantalla.
    """
    os.system("cls" if os.name == "nt" else "clear")

def cargar_sala (n: int, m:int) -> list[list[int]]:
    """
    Genera una matriz con butacas y columnas ingresadas por el usuario.
    Los elementos de la fila se completan con 0s.

    Pre:
        - n: numero entero ingresado por el usuario que representa la cantidad de butacas.
        - m: numero entero ingresado por el usuario que representa la cantidad de columnas.

    Post:
        - devuelve la matriz generada.
    """
    return [[rn.randint(0, 1) for _ in range(m)] for _ in range(n)]

def mostrar_butacas(m: list[list[int]]) -> None:
    """
    Imprime la sala de un cine.

    Pre:
        - m: Matriz de enteros que representa la sala de cine, donde cada lista es una fila de butacas.
    """
    if not m:
        print("La sala está vacía.")
        return
    
    print("         Butacas")
    print("       ", end="")
    print(" ", end="")
    for j in range(len(m[0])):
        print(f"{j+1:2}", end=" ")
    print()
    
    for i, fila in enumerate(m):
        print(f"Fila {i+1:<2} ", end="")
        for butaca in fila:
            print(f"{butaca:2}", end=" ")
        print()

def reservar(m: list[list[int]], f: int, b: int) -> bool:
    """
    Reserva una butaca, solo si esta, está disponible.

    Pre:
        - m: recibe una matriz de numeros enteros la cual se eligiran las butacas.
        - f: entero que representa la fila que el usuario ingresa y desea reservar.
        - b: entero que representa la butaca que el usuario ingresa y desea reservar.

    Post:
        - True: si la butaca es 0, la reserva fue un exito. Y donde estaba el 0 cambia a 1.
        - False: si la butaca es 1, en representacion a que la butaca esta ocupada.
    """
    fila = f - 1
    butaca = b - 1
    
    if m[fila][butaca] == 0:
        m[fila][butaca] = 1
        return True
    else:
        return False
    
def butacas_libres(m: list[list[int]]) -> int:
    """
    Muestra la cantidad de butacas libres en toda la sala.

    Pre:
        - m: matriz en representacion a la sala donde se veran las butacas libres.

    Post:
        - butacas_desocupadas: entero que representa la cantidad de butacas desocupadas que hay en la sala (matriz).
    """
    butacas_desocupadas = 0
    for fila in m:
        for b in fila:
            if b == 0:
                butacas_desocupadas += 1
    return butacas_desocupadas

def butacas_contiguas(m: list[list[int]]) -> Tuple[tuple, int]:
    """
    Busca la fila con butacas libres contiguas mas larga.

    Pre:
        - m: matriz donde se buscara la fila con butacas libres contiguas mas larga.
    
    Post:
        - inicio_max: tupla que contiene la fila (i) con las butacas contiguas mas largas.
                    y la columna (inicio) donde se inicio a contar la ilera de butacas.
        - contiguo_max: entero que representa la cantidad de veces consecutivas que hubo butacas libres.
    """
    contiguo_max = 0
    inicio_max = 0

    for i, fila in enumerate(m):
        contiguo = 0
        inicio = 0
        for j, butaca in enumerate(fila):
            if butaca == 0:
                if contiguo == 0:
                    inicio = j
                contiguo += 1
                if contiguo_max < contiguo:
                    contiguo_max = contiguo
                    inicio_max = (i + 1, inicio + 1)
            else:   
                contiguo = 0

    return inicio_max, contiguo_max
    
def opciones() -> None:
    print("Opcion 1: Generar filas y butacas de la sala.")
    print("Opcion 2: Mostrar butacas.")
    print("Opcion 3: Reservar butaca.")
    print("Opcion 4: Ver butacas desocupadas.")
    print("Opcion 5: Ver butacas contiguas.")
    print("Opcion 0: Salir.")

def menu() -> None:
    sala = list()

    while True:
        opciones()
        op = int(input("\nIngrese una opcion: "))
        limpiar_pantalla()

        if op == 0:
            print("Saliendo...")
            break
        
        elif op == 1:
            print("\n --GENERAR SALA--\n")

            n = int(input("Ingresa la cantidad de filas: "))
            m = int(input("Ingresa la cantidad de butacas: "))

            sala = cargar_sala(n, m)

            salir()

        elif op == 2:
            print("\n--MOSTRAR BUTACAS--\n")
            if sala:
                mostrar_butacas(sala)
            else:
                print("La sala esta vacia.")
            
            salir()
        
        elif op == 3:
            print("\n--RESERVAR BUTACA--\n")
            if sala:
                mostrar_butacas(sala)
                f = int(input("\nIngresa la fila que desea: "))
                b = int(input("Ingresa la butaca que desea: "))

                butacas = len(sala)
                butacas = len(sala[0])

                if  1 <= f <= butacas and 1 <= b <= butacas:
                    reserva = reservar(sala, f, b)
                    if reserva:
                        print("\nLa reserva fue un exito!\n")

                        mostrar_butacas(sala)
                    else:
                        print("\nNo se pudo realizar la reserva :(")
                else:
                    print("Debe ingresar una fila / butaca valida.")
            else:
                print("La sala esta vacia.")
            salir()

        elif op == 4:
            print("\n--VER BUTACAS LIBRES--\n")
            if sala:
                libres = butacas_libres(sala)
                if libres:
                    print(f"\nHay {libres} butacas libres en la sala.")
                else:
                    print("Las butacas estan todas ocupadas.")
            else:
                print("La sala esta vacia.")
            salir()
        
        elif op == 5:
            print("\n--VER BUTACAS CONTIGUAS--\n")
            if sala:
                mostrar_butacas(sala)
                inicio, contiguo = butacas_contiguas(sala)
                f, b = inicio
                print(f"\nLa fila con secuencia mas larga de butacas libres contiguas es la fila -> {f}")
                print(f"El inicio de las butacas libres es la butaca -> {b}")
                print(f"Con {contiguo} butacas de consecutivas.")
            else:
                print("La sala esta vacia.")
            salir()

def main() -> None:
    menu()

if __name__ == "__main__":
    main()