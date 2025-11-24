def convertir_binario(binario: int, contador: int = 0) -> int:
    """
    Convierte un binario a decimal.

    Pre:
        - binario: recibe un número binario ingresado por el usuario.
        - contador: recibe un numero entero que representa el contador que se utilizará como el peso posicional del binario.

    Post:
        retorna un entero que representa el binario convertido en decimal.
    """
    if binario == 0:
        return 0
    ultimo = binario % 10
    resultado = ultimo * (2** contador)
    return resultado + convertir_binario(binario//10, contador + 1)


def main() -> None:
    """
    Funcion principal del programa.
    """
    while True:
        try:
            numero = int(input("Ingrese un número binario (0 y 1): "))
            numero_str = str(numero)
            es_binario = True

            for n in numero_str:
                if n not in ["1", "0"]:
                    print("\nDebe ingresar un numero binario.\n")
                    es_binario = False
                    break
            if es_binario:
                numero_int = int(numero_str)
                convertir = convertir_binario(numero_int)
                print(convertir)
                break
        except ValueError:
            print("\nERROR. Debe ingresar un número entero.\n")

if __name__ == "__main__":
    main()