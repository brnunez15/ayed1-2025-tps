import random as rn
from random import randint

def generar_numero() -> int:
    return rn.randint(1,10)

def cargar_matriz(n: int) -> list[list[int]]:
    return[[generar_numero() for _ in range(n)] for _ in range(n)]

def ordenar_ascendente(matriz: list[list[int]]):
    for i, fila in enumerate(matriz):
        matriz[i] = sorted(fila)
    return matriz

def intercambiar_filas(fila1: int, fila2: int, matriz):
    fila1 -= 1
    fila2 -= 1
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

def intercambiar_columnas(columna1: int, columna2: int, matriz):
    columna1 -= 1
    columna2 -= 1
    for fila in matriz:
        fila[columna1], fila[columna2] = fila[columna2], fila[columna1]
    return matriz

def trasponer_matriz(matriz):
    filas = len(matriz)
    for i in range(filas):
        for j in range(i + 1, filas):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

def promedio_fila(fila: int, matriz):
    cantidad = 0
    total = 0
    for num in matriz[fila]:
        cantidad += 1
        total += num
    promedio = total / cantidad
    return promedio

def calcular_porcentaje (columna: int, matriz):
    filas = len(matriz)
    impares = list()

    for i in range(filas):
        if matriz[i][columna] % 2 != 0:
            impares.append(matriz[i][columna])

    porcentaje = len(impares) / filas * 100
    return porcentaje

def es_simetrica(matriz1):
    original = matriz1
    matriz_transpuesta = trasponer_matriz(matriz1)
    pass

def opciones():
    print("Opcion 0: Salir")
    print("Opcion 1: Cargar numeros enteros en una matriz.")
    print("Opcion 2: Ordenar de forma ascendente cada una de las filas de la matriz.")
    print("Opcion 3: Intercambiar dos filas, cuyos numeros se reciben como parametro.")
    print("Opcion 4: Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.")
    print("Opcion 5: Trasponer la matriz sobre si misma.")
    print("Opcion 6: Calcular el promedio de los elementos de una fila.")
    print("Opcion 7: Calcular el porcentaje de elementos con valor impar en una columna.")
    print("Opcion 8: Determinar si la matriz es simétrica con respecto a su diagonal principal.")
    print("Opcion 9: Determinar si la matriz es simétrica con respecto a su diagonal secundaria.")
    print("Opcion 10: Determinar qué columnas de la matriz son palíndromos (capicúas).")

def menu():
    while True:
        opciones()
        op = int(input("\nIngrese una opcion: "))
        if op == 0:
            print("Saliendo...")
            break
        if op == 1:
            n = int(input("Ingrese un numero: "))
            matriz = cargar_matriz(n)
            print(f"\nMatriz cargada con numeros aleatorios: {matriz} \n")
        
        elif op == 2:
            matriz_ordenada = ordenar_ascendente(matriz)
            print(f"\nMatriz ordenada: {matriz_ordenada}\n")

        elif op == 3:
            filas = len(matriz)

            while True:
                fila_1 = int(input("Ingrese la primer fila a intercambiar: "))
                fila_2 = int(input("Ingrese la segunda fila a intercambiar: "))
        
                if  1 <= fila_1 <= filas and 1 <= fila_2 <= filas:
                    matriz_intercambiada = intercambiar_filas(fila_1, fila_2, matriz)
                    print(f"\nMatriz con filas intercambiadas: {matriz_intercambiada}\n")
                    break

                print(f"Debe ingresar una cantidad de filas validas\n") 

        elif op == 4:
            #falta agregar validacion
            print("Columnas 1 y 2 intercambiadas: ")
            matriz_columnas = intercambiar_columnas(1, 2, matriz)
            for f in matriz_columnas:
                print(f)

        elif op == 5:
            matriz_transpuesta = trasponer_matriz(matriz)
            print("Matriz transpuesta: ")
            for i, fila in enumerate(matriz_transpuesta):
                print(f"Fila {i}: {fila}")

        elif op == 6:
            num = int(input("\nIngrese la fila que desee el promedio: "))
            promedio= promedio_fila(num,matriz)
            print(f"El promedio de la fila {num} es: {promedio:.2f}\n")

        elif op == 7:
            col = int(input("Ingrese una columna: "))
            porcentaje = calcular_porcentaje(col, matriz)
            print(f"{porcentaje:.2f}")

        elif op == 8:
            pass

        elif op == 9:
            pass

        elif op == 10:
            pass

def main():
    menu()
    
if __name__ == "__main__":
    main()