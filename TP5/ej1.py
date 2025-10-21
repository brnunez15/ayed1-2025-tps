class NumeroNegativo(Exception):
    "Indica que un numero es negativo."

def main() -> None:
    try:
        numero = int(input("Ingrese un numero entero positivo: "))
        print(f"El numero ingresado es: {numero}")

        if numero < 0:
            raise NumeroNegativo("El numero debe ser un entero positivo.")
        
    except ValueError:
        print("Debe ingresar un numero entero.")

if __name__ == "__main__":
    main()