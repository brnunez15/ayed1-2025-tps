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

def main():
    n = int(input("Ingrese un numero: "))
    matriz = cargar_matriz(n)
    print(f"\nMatriz cargada con numeros aleatorios: {matriz}")

    matriz_ordenada = ordenar_ascendente(matriz)
    print(f"\nMatriz ordenada: {matriz_ordenada}\n")

    filas = len(matriz)

    while True:
        fila_1 = int(input("Ingrese la primer fila a intercambiar: "))
        fila_2 = int(input("Ingrese la segunda fila a intercambiar: "))
        
        if  1 <= fila_1 <= filas and 1 <= fila_2 <= filas:
            matriz_intercambiada = intercambiar_filas(fila_1, fila_2, matriz)
            print(f"\nMatriz con filas intercambiadas: {matriz_intercambiada}\n")
            break
        print(f"Debe ingresar una cantidad de filas validas\n")

    #falta agregar validacion
    print("Columnas 1 y 2 intercambiadas: ")
    matriz_columnas = intercambiar_columnas(1, 2, matriz)
    for f in matriz_columnas:
        print(f)
    print()

    matriz_transpuesta = trasponer_matriz(matriz)
    print("Matriz transpuesta: ")
    for i, fila in enumerate(matriz_transpuesta):
        print(f"Fila {i}: {fila}")

    num = int(input("\nIngrese la fila que desee el promedio: "))
    promedio= promedio_fila(num,matriz)
    print(f"El promedio de la fila {num} es: {promedio:.2f}\n")

    col = int(input("Ingrese una columna: "))
    porcentaje = calcular_porcentaje(col, matriz)
    print(f"{porcentaje:.2f}")
if __name__ == "__main__":
    main()