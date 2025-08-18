es_triangular = lambda n: any(i * (i + 1) // 2 == n for i in range(1, n + 1))

def main():
    n = int(input("Ingrese un número: "))
    if es_triangular(n) == True:
        print(f"El número {n} es triangular")
    else:
        print(f"El número {n} no es triangular")

if __name__ == "__main__":
    main()