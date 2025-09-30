import random as rn
from random import randint
import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def generar_numero() -> int:
    return rn.randint(1,10)

def cargar_matriz(n: int) -> list[list[int]]:
    return[[generar_numero() for _ in range(n)] for _ in range(n)]

def ordenar_ascendente(matriz: list[list[int]]):
    nueva = [fila[:] for fila in matriz]
    for i, fila in enumerate(nueva):
        nueva[i] = sorted(fila)
    return nueva

def intercambiar_filas(fila1: int, fila2: int, matriz):
    fila1 -= 1
    fila2 -= 1
    nueva = [fila[:] for fila in matriz]
    nueva[fila1], nueva[fila2] = nueva[fila2], nueva[fila1]
    return nueva

def intercambiar_columnas(columna1: int, columna2: int, matriz):
    columna1 -= 1
    columna2 -= 1
    nueva = [fila[:] for fila in matriz]
    for fila in nueva:
        fila[columna1], fila[columna2] = fila[columna2], fila[columna1]
    return nueva

def trasponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = [[0]*filas for _ in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]

    return transpuesta

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

def es_simetrica_principal(matriz):
    n = len(matriz)
    for f in range(n):
        for c in range(n):
            if matriz[f][c] != matriz[c][f]:
                return False
    return True

def es_simetrica_secundaria(matriz):
    n = len(matriz)
    for f in range(n):
        for c in range(n):
            if matriz[f][c] != matriz[n - c - 1][n - f - 1]:
                return False
    return True

def es_capicua(matriz):
    largo_f = len(matriz)   
    largo_c = len(matriz[0])
    columnas = list()
    for c in range(largo_c):
        columna = [matriz[f][c] for f in range(largo_f)]
        if columna == columna[::-1]:
            columnas.append(c)
    return columnas

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
    matriz = list()

    while True:
        opciones()
        op = int(input("\nIngrese una opcion: "))
        limpiar_pantalla()

        if op == 0:
            print("Saliendo...")
            break

        if op == 1:
            while True:
                
                print("\n--CARGAR MATRIZ--\n")
                n = int(input("Ingrese un numero: "))
                matriz = cargar_matriz(n)
                print(f"\nMatriz cargada con numeros aleatorios: \n")
                for i, fila in enumerate(matriz):
                    print(f"Fila {i + 1}: {fila}")
                
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break
        
        elif op == 2:

            print("\n--MATRIZ ORDENADA--\n")
            while True:

                if matriz:

                    matriz_ordenada = ordenar_ascendente(matriz)

                    print(f"Matriz original: \n")

                    for i, fila in enumerate(matriz):
                        print(f"Fila {i}: {fila}")

                    print(f"\nMatriz ordenada: \n")
                    
                    for i, fila in enumerate(matriz_ordenada):
                        print(f"Fila {i}: {fila}")
                    
                    
                else:
                    print("No hay una matriz cargada\n")
                    
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 3:
            print("\n--INTERCAMBIAR FILAS--\n")

            while True:
                if matriz:
                    filas = len(matriz)

                    while True:

                        print("\nMatriz original: \n")
                        for i, fila in enumerate(matriz):
                            print(f"Fila {i+1}: {fila}")

                        fila_1 = int(input("\nIngrese la primer fila a intercambiar: "))
                        fila_2 = int(input("Ingrese la segunda fila a intercambiar: "))
                
                        if  1 <= fila_1 <= filas and 1 <= fila_2 <= filas:
                            matriz_intercambiada = intercambiar_filas(fila_1, fila_2, matriz)

                            print(f"\nMatriz con filas intercambiadas: \n")
                            for i, fila in enumerate(matriz_intercambiada):
                                print(f"Fila {i+1}: {fila}")
                            break

                        else:
                            print(f"\nDebe ingresar una cantidad de filas validas\n") 
                else:
                    print("No hay una matriz cargada\n")

                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 4:

            print("\n--INTERCAMBIAR COLUMNAS--\n")

            while True:

                if matriz:
                    
                    print("\nMatriz original: \n")

                    for i, f in enumerate(matriz):
                        print(f"Fila {i + 1}: {f}")

                    col1 = int(input("\nIngrese la primer columna: "))
                    col2 = int(input("Ingrese la segunda columna: "))

                    columnas = len(matriz[0])

                    if 1 <= col1 <= columnas and 1 <= col2 <= columnas:

                        print(f"\nColumnas {col1} y {col2} intercambiadas: ")
                        matriz_columnas = intercambiar_columnas(col1, col2, matriz)
                        for f in matriz_columnas:
                            print(f)
                    else:
                        print("Debe ingresar una cantidad de columnas valida.")
                else:
                    print("No hay una matriz cargada\n")

                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 5:

            while True:

                print("\n--TRANSPONER MATRIZ--")

                if matriz:

                    print("\nMatriz original: \n")

                    for i, f in enumerate(matriz):
                        print(f"Fila {i + 1}: {f}")

                    matriz_transpuesta = trasponer_matriz(matriz)

                    print("\nMatriz transpuesta: \n")

                    for i, fila in enumerate(matriz_transpuesta):
                        print(f"Fila {i+1}: {fila}")
                else:
                    print("No hay una matriz cargada\n")
                
                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 6:

            print("\n--PROMEDIO DE UNA FILA--\n")
            while True:
                if matriz:

                    print("\nMatriz original: \n")

                    for i, f in enumerate(matriz):
                        print(f"Fila {i + 1}: {f}")

                    filas = len(matriz)

                    num = int(input("\nIngrese la fila que desee el promedio: "))

                    if 1 <= num <= filas:
                        promedio= promedio_fila(num - 1 , matriz)
                        print(f"El promedio de la fila {num} es: {promedio:.2f}\n")
                    else:
                        print("Debe ingresar una fila valida")
                else:
                    print("No hay una matriz cargada\n")
                
                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 7:
            print("\n--PORCENTAJE DE VALORES IMPARES DE UNA COLUMNA--\n")
            while True:

                if matriz:

                    print("\nMatriz original: \n")

                    for i, f in enumerate(matriz):
                        print(f"Fila {i + 1}: {f}")

                    columnas = len(matriz[0])
                    col = int(input("Ingrese una columna: "))

                    if 1 <= col <= columnas:

                        porcentaje = calcular_porcentaje(col - 1, matriz)
                        print(f"El porcentaje de la columna {col} es de: {porcentaje:.2f}")
                    else:
                        print("Debe ingresar una cantidad de columnas validas")

                else:
                    print("No hay una matriz cargada\n")
                
                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 8:

            print("\n--SIMETRIA SEGUN SU DIAGONAL PRINCIPAL")

            while True:

                if matriz:

                    print("\nMatriz original: \n")

                    for i, f in enumerate(matriz):
                        print(f"Fila {i + 1}: {f}")

                    if es_simetrica_principal(matriz):
                        print(f"\nLa matriz es simetrica segun su diagonal principal.")
                    else:
                        print(f"\nLa matriz no es simetrica segun su diagonal principal.")
                else:
                    print("No hay una matriz cargada\n")
                
                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 9:

            print("\n--SIMETRIA SEGUN SU DIAGONAL SECUNDARIA")
            
            while True:

                if matriz:

                    print("\nMatriz original: \n")

                    for i, f in enumerate(matriz):
                        print(f"Fila {i + 1}: {f}")

                    if es_simetrica_secundaria(matriz):
                        print(f"\nLa matriz es simetrica")
                    else:
                        print(f"\nLa matriz no es simetrica.")
                
                else:
                    print("No hay una matriz cargada\n")
                
                salir = int(input("\nIngrese 0 para volver al menu: "))

                if salir == 0:
                    break

        elif op == 10:

            print("\n--VER COLUMNAS CAPICUAS--\n")

            while True:

                if matriz:

                    print("\nMatriz original: \n")

                    for i, f in enumerate(matriz):
                        print(f"Fila {i + 1}: {f}")

                    columnas_capicuas = es_capicua(matriz)

                    print(f"\nLas columnas capicuas de la matriz son: {columnas_capicuas}")

                else:
                    print("No hay una matriz cargada\n")
                
                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break

        else:
            print(f"Opcion incorrecta")
            
def main():
    menu()
    
if __name__ == "__main__":
    main()