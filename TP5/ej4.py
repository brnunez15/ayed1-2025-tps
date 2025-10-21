import time

def main() -> None:
    """
    Incrementa un numero hasta llegar al 10.000 y en cada incrementacion espera 0,05s.
    Si el usuario interrumpe, el programa captura un error.
    """
    num = 1
    while True:
        try:
            print(num)
            time.sleep(0.05)
            num += 1
            if num > 100000:
                break

        except KeyboardInterrupt:
            opcion = input("\nDesea interrumpir la ejecución? (si/no): ")
            if opcion.lower() == "si":
                print("Programa interrumpido por el usuario.")
                break

if __name__ == "__main__":
    main()