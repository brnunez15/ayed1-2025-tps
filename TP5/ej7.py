import random as rn

def generar_numero() -> int:
    """
    Genera un numero aleatorio entre 1 y 500.
    """
    return rn.randint(1, 500)

def main() -> None:
    """
    El usuario debe ingresar un numero e ir adivinando segun la guia que le da el programa.
    Cuenta la cantidad de intentos.
    """
    numero_programa = generar_numero()
    intentos = 0
    print("\nEl programa ha generado un numero. Intenta adivinarlo!!\n")

    while True:
        try:
            numero_usuario = int(input("Ingrese un numero del 1 al 500: "))
            intentos += 1
            if numero_usuario > numero_programa:
                print("\nEl numero que ingreso es mayor al numero que se genero.")
            elif numero_usuario < numero_programa:
                print("\nEl numero que ingreso es menor al que se genero.")
            else:
                print(f"\nAdivino el numero!! {numero_programa}")
                print(f"Cantidad de intentos hasta adivinar: {intentos}")
                break

        except ValueError:
            print("Debe ingresar un numero entero")
if __name__ == "__main__":
    main()