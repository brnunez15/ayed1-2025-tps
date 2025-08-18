es_oblongo = lambda n: any(i * (i + 1) == n  for i in range(1, n))

def main ():
    n = int(input("Ingrese un numero: "))
    if es_oblongo(n) == True:
        print(f"El número {n} es oblongo")
    else:
        print (f"El número {n} no es oblongo")

if __name__ == "__main__":
    main()