import random as rn

def generar_numeros():
    return rn.randint(0, 150)

def generar_matriz(n: int):
    return [[generar_numeros() for _ in range(6)] for _ in range(n)]

def mas_producida(matriz):
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
def opciones():
    print("Opcion 1: Ingresar las fabricas.")
    print("Opcion 2: Cantidad total de bicicletas fabricadas por cada fabrica")
    print("Opcion 3: Fabrica que mas produjo en un solo dia.")
    print("Opcion 4: Dia mas productivo.")
    print("Opcion 5: El dia con menos produccion de cada fabrica.")

def menu():
    while True:
        opciones()
        op = int(input("Ingrese una opcion: "))
        if op == 0:
            print("Saliendo...")
            break
        elif op == 1:
            n = int(input("Ingrese la cantidad de fabricas: "))
            matriz = generar_matriz(n)
            for i, fila in enumerate(matriz):
                print(f"Fabrica {i + 1}: {fila}")
        elif op == 2:
            for i, fila in enumerate (matriz):
                total = sum(fila)
                print(f"Fabrica {i + 1}: {fila} | Total: {total}")
        elif op == 3:
            bicis, fabrica, dia = mas_producida(matriz)
            print(f"Fabrica que mas produjo en un dia: Fabrica {fabrica + 1}")
            print(f"Produjo: {bicis} bicicletas, el dia {dia}")

def main ():
    menu()

if __name__ == "__main__":
    main()