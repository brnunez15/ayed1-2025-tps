from typing import List

def gen_matriz (n: int) -> List[list[int]]:
    return [[0 for _ in range(n)] for _ in range(n)]

def copiar(m):
    nueva = [[elem for elem in sublista] for sublista in m]
    return nueva

def patron_a(m: list[list[int]]):
    nueva = copiar(m)
    largo = len(nueva)
    n = 1
    for f in range(largo):
        for c in range(largo):
            if f == c:
                nueva[f][c] = n
                n += 2
    return nueva

def patron_b(m: list[list[int]]):
    nueva = copiar(m)
    largo = len(nueva)
    for f in range(largo):
        for c in range(largo):
            if f + c == largo - 1:
                nueva[f][c] = 3 ** (largo - 1 - f)
    return nueva

def patron_c(m: list[list[int]]):
    nueva = copiar(m)
    largo = len(nueva)
    n = largo
    for f in range(largo):
        punto = n
        for c in range(largo):
            if f == c:
                nueva[f][c] = punto
                n -= 1
            elif c < f:
                nueva[f][c] = punto
    return nueva

def patron_d(m:list[list[int]]):
    nueva = copiar(m)
    largo = len(nueva)
    n = largo
    for f in range(largo):
        for c in range(largo):
            nueva[f][c] = 2 ** (n - 1)
        n -= 1
    return nueva

def patron_e(m:list[list[int]]):
    nueva = copiar(m)
    filas = len(nueva)
    columnas = len(nueva[0])
    n = 0
    for f in range(filas):
        for c in range(columnas):
            if f == c:
                nueva[f][c] = 0
            elif f < c:
                nueva[f][c] = 0
                nueva[c][f] = 0
    
    for f in range(filas):
        for c in range(columnas):
            if (f + c) % 2 != 0:
                n +=1
                nueva[f][c] = n
    return nueva

def main():
    n = int(input("Ingrese un numero: "))

    matriz_gral = gen_matriz(n)
    for f in (matriz_gral):
        print(f)
    print()

    a = patron_a(matriz_gral)
    for f in (a):
        print (f)
    print()

    b = patron_b(matriz_gral)
    for f in (b):
        print(f)
    print()

    c = patron_c(matriz_gral)
    for f in (c):
        print(f)
    print()

    d = patron_d(matriz_gral)
    for f in (d):
        print(f)
    print()

    e = patron_e(matriz_gral)
    for f in (e):
        print(f)
if __name__ == "__main__":
    main()