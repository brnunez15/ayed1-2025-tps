from typing import Tuple

def validar_fecha(fecha: Tuple[int, int]) -> bool:
    """
    Valida una fecha recibida como tupla (día, mes).

    Pre: 
        - Recibe una tupla de 2 enteros positivos.
    Post: 
        - Devuelve True si la fecha es válida.
    """
    dia, mes = fecha

    es_valida = True

    if not (1 <= mes <= 12):
        es_valida = False

    else:
        if mes in (1, 3, 5, 7, 8, 10, 12):
            es_valida = 1 <= dia <= 31

        elif mes in (4, 6, 9, 11):
            es_valida = 1 <= dia <= 30

    return es_valida

def pasar_fecha_string(fecha: tuple[int,int,int]) -> str:
    """
    Devuelve una fecha en formato extendido.
    Si el año tiene dos digitos, se interpreta segun el año de corte.

    Pre:
        - fecha: tupla donde contiene 3 enteros (dia, mes, anio),
    
    Post:
        - Devuelve una cadena con la fecha en formato extendido.
    """
    corte = 30
    d, m, a = fecha
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Diciembre")
    nombre_mes = ""
    for i, mes in enumerate(meses):
        if i + 1 == m:
            nombre_mes += mes
            break

    if 0 <= len(str(a)) <= 2:
        if a > corte:
            a += 1900
        else:
            a += 2000

    return f"{d} de {nombre_mes} de {a}"

def main() -> None:
    """
    Funcion principal del programa.
    """
    while True:
        try:
            dia = int(input("Ingrese el dia: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))

            if validar_fecha((dia, mes)):
                f = pasar_fecha_string((dia, mes, anio))
                print(f"La fecha ingresada es: {f}")
                break
            print("\nFecha invalida. Intentelo de nuevo\n")

        except ValueError:
            print("\nERROR. Debe ingresar un numero entero valido.\n")

if __name__ == "__main__":
    main()