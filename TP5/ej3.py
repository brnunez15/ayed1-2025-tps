class ErrorMesInvalido(Exception):
    """
    Indica un error que el mes es invalido.
    """

def mes (numero_mes: int) -> str:
    """
    Devuelve el nombre del mes correspondiente al numero de mes recibido.

    Pre:
        - numero_mes: entero que representa a un mes.
    
    Post:
        - m: devuelve el nombre del mes correspondiente al numero de mes recibido.
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    for i, m in enumerate(meses):
        if numero_mes - 1 == i:
            return m
        
    raise ErrorMesInvalido("El numero del mes debe ser entre 1 y 12.")

def main() -> None:
    try:
        num_mes = int(input("Ingrese un numero del mes: "))
        nombre_mes = mes(num_mes)
        print(f"El nombre correspondiente al mes {num_mes} es: {nombre_mes}")

    except ValueError:
        print("Debe ingresar un numero entero.")

    except ErrorMesInvalido as e:
        print(e)
        print("")

if __name__ == "__main__":
    main()