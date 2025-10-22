"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. c. Sumar N días a una fecha.
Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""
from typing import Tuple

def validar_fecha(fecha: Tuple[int, int, int]) -> bool:
    """
    Valida una fecha recibida como tupla (día, mes, año).

    Pre: 
        - Recibe una tupla de 3 enteros positivos.
    Post: 
        - Devuelve True si la fecha es válida.
    """
    dia, mes, anio = fecha

    es_valida = True
    
    if not (1900 <= anio <= 2025):
        es_valida = False

    elif not (1 <= mes <= 12):
        es_valida = False

    else:
        if mes in (1, 3, 5, 7, 8, 10, 12):
            es_valida = 1 <= dia <= 31

        elif mes in (4, 6, 9, 11):
            es_valida = 1 <= dia <= 30

        elif mes == 2:
            if es_bisiesto(anio):
                es_valida = 1 <= dia <= 29
            else:
                es_valida = 1 <= dia <= 28
    
    return es_valida


def es_bisiesto (anio: int) -> bool:
    """
    Verifica si un año ingresado es bisiesto, o no.

    Pre: El número ingresado tiene que ser un entero positivo.

    Post: Retornará (True) si el año es bisiesto. Por lo contrario retorna (False).
    """
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

def ingresar_fecha () -> tuple:
    """
    Permite que el usuario ingrese una fecha con numeros enteros, ya sea valida o no.

    Post: devuelve 3 números enteros que representan a la fecha ingresada.
    """
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    return dia, mes, anio

def main() -> None:
    """
    Funcion principal del programa.
    """
    dia, mes, anio = ingresar_fecha()

    validar = validar_fecha((dia, mes, anio))

    if validar:
        print(f"La fecha {dia}/{mes}/{anio} es valida")
    else:
        print(f"La fecha {dia}/{mes}/{anio} es invalida")

if __name__ == "__main__":
    main()