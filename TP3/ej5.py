def generar_matriz (n: int, m:int) -> list[list[int]]:
    return [[0 for _ in range(m)] for _ in range(n)]

def mostrar_butacas(m: list[list[int]]) -> None:
    if not m:
        print("La sala está vacía.")
        return
    
    print("       Butacas")
    print("       ", end="")
    for j in range(len(m[0])):
        print(f"{j+1:2}", end=" ")
    print()
    
    for i, fila in enumerate(m):
        print(f"Fila {i+1:<2} ", end="")
        for butaca in fila:
            simbolo = "O" if butaca == 0 else "X"
            print(f"{simbolo:2}", end=" ")
        print()

def reservar(m: list[list[int]], f: int, b: int):

    fila = f - 1
    butaca = b - 1
    
    if m[fila][butaca] == 0:
        m[fila][butaca] = 1
        return True
    else:
        return False

def menu():
    sala = list()

    while True:
        op = int(input("\nIngrese una opcion: "))

        if op == 0:
            print("Saliendo...")
            break
        
        elif op == 1:
            print("\n --GENERAR SALA--\n")

            n = int(input("Ingresa la cantidad de filas: "))
            m = int(input("Ingresa la cantidad de butacas: "))

            sala = generar_matriz(n, m)
        
        elif op == 2:
            print("\n--MOSTRAR BUTACAS--\n")
            if sala:
                mostrar_butacas(sala)
            else:
                print("La sala esta vacia.")
        
        elif op == 3:

            f = int(input("Ingresa la fila que desea: "))
            b = int(input("Ingresa la butaca que desea: "))

            filas = len(sala)
            butacas = len(sala[0])

            if  1 <= f <= filas and 1 <= b <= butacas:
                reservar(sala, f, b)
            else:
                print("Debe ingresar una fila / butaca valida.")

def main():
    menu()

if __name__ == "__main__":
    main()