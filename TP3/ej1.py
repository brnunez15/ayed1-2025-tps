import random as rn
from random import randint
import os
from typing import List

def limpiar_pantalla() -> None:
    """
    Funcion para limpiar pantalla.
    """
    os.system("cls" if os.name == "nt" else "clear")

def generar_numero() -> int:
    """
    Genera un numero entero aleatorio entre el 1, 10.

    Post: retorna un entero aleatorio.
    """
    return rn.randint(1,10)

def cargar_matriz(n: int) -> list[list[int]]:
    """
    Carga una matriz ingresando N desde el usuario.

    Pre: recibe un entero representando la cantidad de filas y columnas.

    Post: devuelve la matriz generada.
    """
    return[[generar_numero() for _ in range(n)] for _ in range(n)]

def ordenar_ascendente(matriz: list[list[int]]) -> List[list[int]]:
    """
    Ordena todas las filas de una matriz de forma ascendente.

    Pre: recibe la matriz a ordenar.

    Post: devuelve una copia de la matriz original, de manera ordenada ascendentemente.
    """
    nueva = [fila[:] for fila in matriz]
    for i, fila in enumerate(nueva):
        nueva[i] = sorted(fila)
    return nueva

def intercambiar_filas(fila1: int, fila2: int, matriz: list[list[int]]) -> List[list[int]]:
    """
    Intercambia las posiciones de dos filas, de una matriz.

    Pre: recibe las dos filas a intercambiar, ingresadas por el usuario.
        Tambien recibe la matriz que se tomara de referencia.
    
    Post: devuelve una copia de la matriz, con sus filas intercambiadas.
    """
    fila1 -= 1
    fila2 -= 1
    nueva = [fila[:] for fila in matriz]
    nueva[fila1], nueva[fila2] = nueva[fila2], nueva[fila1]
    return nueva

def intercambiar_columnas(columna1: int, columna2: int, matriz: list[list[int]]) -> List[list[int]]:
    """
    Intercambia las posiciones de dos columnas, de una matriz.

    Pre:
        - columna1: entero, ingresado por el usuario representando una posicion de una columna.
        - columna2: entero, ingresado por el usuario representando una posicion de una columna.
        - matriz: matriz que se tomara como referencia.

    Post:
        - nueva: devuelve una copia de la matriz recibida con sus columnas intercambiadas.
    """
    columna1 -= 1
    columna2 -= 1
    nueva = [fila[:] for fila in matriz]
    for fila in nueva:
        fila[columna1], fila[columna2] = fila[columna2], fila[columna1]
    return nueva

def trasponer_matriz(matriz: list[list[int]]) -> List[list[int]]:
    """
    Transpone una matriz. Es decir, convierte las filas en columnas y las columnas en filas.

    Pre:
        - matriz: recibe la matriz que se tomara de referencia para transponerla.
    
    Post:
        - transpuesta: devuelve una copia de la matriz recibida, con sus elementos transpuestos.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[0]*filas for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

def promedio_fila(fila: int, matriz: list[list[int]]) -> int:
    """
    Calcula el promedio de todos los elementos de una fila.

    Pre:
        - fila: recibe un entero ingresado por el usuario, representando la posicion de una fila.
        - matriz: recibe la matriz de referencia.
    
    Post: 
        - promedio: devuelve el promedio calculado de los elementos de una fila.
    """
    cantidad = 0
    total = 0
    for num in matriz[fila]:
        cantidad += 1
        total += num
    promedio = total / cantidad
    return promedio

def calcular_porcentaje (columna: int, matriz: list[list[int]]) -> int:
    """
    Calcula el porcentaje de elementos con valor impar de una columna.

    Pre:
        - columna: entero ingresado por el usuario, representando la posicion de una columna.
        - matriz: matriz de referencia para obtener los datos.

    Post:
        - porcentaje: devuelve el resultado del porcentaje de todos los impares de una columna.
    """
    filas = len(matriz)
    impares = list()

    for i in range(filas):
        if matriz[i][columna] % 2 != 0:
            impares.append(matriz[i][columna])

    porcentaje = len(impares) / filas * 100
    return porcentaje

def es_simetrica_principal(matriz: list[list[int]]) -> bool:
    """
    Verifica si una matriz es simetrica segun su diagonal principal.

    Pre:
        - recibe la matriz a verificar.
    
    Post:
        - True: en caso de que la matriz sea simetrica
        - False: en caso contrario.
    """
    n = len(matriz)
    for f in range(n):
        for c in range(n):
            if matriz[f][c] != matriz[c][f]:
                return False
    return True

def es_simetrica_secundaria(matriz: list[list[int]]) -> bool:
    """
    Verifica si una matriz es simetrica segun su diagonal secundaria.

    Pre:
        - recibe la matriz a verificar.
    
    Post:
        - True: en caso de que la matriz sea simetrica
        - False: en caso contrario.
    """
    n = len(matriz)
    for f in range(n):
        for c in range(n):
            if matriz[f][c] != matriz[n - c - 1][n - f - 1]:
                return False
    return True

def es_capicua(matriz: list[list[int]]) -> List[int]:
    """
    Comprueba si las columnas de una matriz son capicuas y muestra las columnas que lo son.

    Pre:
        - matriz: recibe la matriz a comprobar.
    
    Post:
        - columnas: lista de enteros, representando las columnas capicuas de la matriz.
    """
    largo_f = len(matriz)   
    largo_c = len(matriz[0])
    columnas = list()
    for c in range(largo_c):
        columna = [matriz[f][c] for f in range(largo_f)]
        if columna == columna[::-1]:
            columnas.append(c)
    return columnas

def opciones() -> None:
    """
    Mustra todas las opciones del menu.
    """
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

def menu() -> None:
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
                    if columnas_capicuas:
                        print(f"\nLas columnas capicuas de la matriz son: {columnas_capicuas}")
                    else:
                        print("\nNo hay columnas capicuas\n")
                else:
                    print("No hay una matriz cargada\n")
                
                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break
        else:
            print(f"Opcion incorrecta")
            
def main() -> None:
    menu()
    
if __name__ == "__main__":
    main()