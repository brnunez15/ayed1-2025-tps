import random as rn
from typing import List, Tuple

def generar_numeros() -> int:
    """
    Genera numeros enteros aleatorios.

    Post: retorna un numero aleatorio entre 0 y 150.
    """
    return rn.randint(0, 150)

def generar_matriz(n: int) -> List[list[int]]:
    """
    Genera una matriz con listas con elementos de numeros enteros aleatorios.

    Pre: recibe la cantidad de filas ingresadas por el usuario.

    Post: Devuelve la matriz generada.
    """
    return [[generar_numeros() for _ in range(6)] for _ in range(n)]

def mas_producida(matriz: List[list[int]]) -> Tuple[int, int, int]:
    """
    Calcula la fabrica que mas produjo, el dia de la misma y cuanto se produjo ese dia.

    Pre: Recibe la matriz por la cual va a ser calculada.

    Post: devuelve una tupla de enteros representando la fabrica, el dia y la cantidad mas producida.
    """
    fabrica_max = -1
    dia_max = -1
    cantidad_max = -1

    for fabrica, fila in enumerate(matriz):
        mayor = max(fila)
        if mayor > cantidad_max:
            cantidad_max = mayor
            fabrica_max = fabrica
            dia_max = fila.index(cantidad_max)

    return cantidad_max, fabrica_max, dia_max

def calcular_dia_mas_productivo(matriz: List[list[int]]) -> Tuple[int, int]:
    """
    Calcula el dia mas producido entre todas las fabricas.

    Pre: Recibe la matriz la cual va a ser calculadas todas sus columnas(dias).

    Post: Devuelve una tupla con la el total y el dia mas producido.
    """
    total_max = -1
    dia_max = -1

    for i, col in enumerate(zip(*matriz)):
        total = sum(col)
        if total_max < total:
            total_max = total
            dia_max = i

    return total_max, dia_max

def calucular_menos_productivo(matriz: List[list[int]]) -> List[int]:
    """
    Calula la cantidad de bicis menos producidas por cada fabrica.

    Pre: recibe la matriz que va a ser calculada.

    Post: devuelve una lista con las cantidades minimas por fabrica.
    """
    return [min(f) for f in matriz]

def opciones() -> None:
    print("Opcion 1: Ingresar las fabricas.")
    print("Opcion 2: Cantidad total de bicicletas fabricadas por cada fabrica")
    print("Opcion 3: Fabrica que mas produjo en un solo dia.")
    print("Opcion 4: Dia mas productivo.")
    print("Opcion 5: El dia con menos produccion de cada fabrica.")

def menu() -> None:
    matriz = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    while True:
        opciones()
        op = int(input("Ingrese una opcion: "))
        if op == 0:
            print("Saliendo...")
            break
        elif op == 1:
            while True:
                n = int(input(f"Ingrese la cantidad de fabricas: "))
                matriz = generar_matriz(n)
                for i, fila in enumerate(matriz):
                    print(f"Fabrica {i + 1}: {fila}")
                
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 2:
            while True:
                if matriz:
                    for i, fila in enumerate (matriz):
                        total = sum(fila)
                        print(f"Fabrica {i + 1}: {fila} | Total: {total}")
                else:
                    print("Aun no hay fabricas ingresadas.")
                
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 3:
            bicis, fabrica, dia = mas_producida(matriz)
            while True:
                if bicis and dia and fabrica != -1:
                    print(f"\nFabrica que mas produjo en un dia: Fabrica {fabrica + 1}")
                    print(f"Produjo: {bicis} bicicletas, el dia {dias[dia]}")
                else:
                    print("Aun no hay bicis producidas")
                
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 4:
            total, dia = calcular_dia_mas_productivo(matriz)
            while True:
                if total and dia != -1:
                    print(f"El dia mas productivo es el dia: {dias[dia]} con {total} producciones.")
                else:
                    print("Aun no hay bicis producidas")
                
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 5:
            while True:
                if matriz:
                    total = calucular_menos_productivo(matriz)
                    for f, t in enumerate(total):
                        print(f"Fabrica {f+1} | Produccion minima {t}.")
                else:
                    print("\nAun no hay fabricas ingresadas.")
                
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break
                
def main() -> None:
    menu()

if __name__ == "__main__":
    main()