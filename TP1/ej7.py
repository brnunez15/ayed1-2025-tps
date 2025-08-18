def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Valida 3 números enteros, el cual debera cumplir con requisitos de una fecha real.

    Pre: Los 3 números ingresados deben ser enteros positivos.

    Post: Devuelve un valor booleano que indica si la fecha es válida (True) o no (False).
    """

    if anio < 1900 or anio > 2025:
            return False

    if mes < 1 or mes > 12:
        return False
    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return dia >= 1 or dia <= 31

    elif mes == 4 or mes == 6 or mes == 9:
        return dia >= 1 or dia <= 30

    if mes == 2:

        if es_bisiesto(anio):  
            return dia >= 1 or dia <= 29

        else:
             return dia >= 1 or dia <= 28


def es_bisiesto (anio: int) -> bool:
     """
     Verifica si un año ingresado es bisiesto, o no.

     Pre: El número ingresado tiene que ser un entero positivo.

     Post: Retornará (True) si el año es bisiesto. Por lo contrario retorna (False).
     """
     return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

def dia_siguiente (dia: int, mes: int, anio: int):

    meses_31 = [1, 3, 5, 7, 8, 10, 12]
    meses_30 = [4, 6, 9, 11]

    if mes in meses_31:
    
        if dia < 31 :
            dia += 1
        else:
            dia = 1
            mes += 1

    elif mes in meses_30:

        if dia < 30:
            dia += 1
        else:
            dia = 1
            mes += 1
    
    elif mes == 2:
        if es_bisiesto(anio):

            if dia < 29:
                dia += 1
            else:
                dia = 1
                mes += 1
        else:
            if dia < 28:
                dia += 1
            else:
                dia = 1
                mes += 1
    if mes > 12:
        mes = 1
        dia = 1
        anio += 1

    return dia, mes, anio

def sumar_dias (dia: int, mes: int, anio: int, n: int):

    for _ in range(n + 1):
        dia, mes, anio = dia_siguiente(dia, mes, anio)

    return dia, mes, anio

def ingresar_fecha () -> int:
     """
     Permite que el usuario ingrese una fecha con numeros enteros, ya sea valida o no.

     Post: devuelve 3 números enteros que representan a la fecha ingresada.
     """
     dia = int(input("Ingrese el dia: "))
     mes = int(input("Ingrese el mes: "))
     anio = int(input("Ingrese el anio: "))
     return dia, mes, anio


def main ():
    dia, mes, anio = ingresar_fecha()
    if validar_fecha(dia, mes, anio) == True:

        dia_sig, mes_sig, anio_sig = dia_siguiente(dia, mes, anio)

        print(f"El dia siguiente de la fecha ingresada es: {dia_sig}/{mes_sig}/{anio_sig}")

        dias_a_sumar = int(input("Ingrese la cantidad de dias a sumar: "))
        dia_nuevo, mes_nuevo, anio_nuevo = sumar_dias(dia, mes, anio, dias_a_sumar)

        print(f"La fecha luego de agregar {dias_a_sumar} dia/s es: {dia_nuevo}/{mes_nuevo}/{anio_nuevo}")
    else:
        print("Debe ingresasar una fecha valida")

if __name__ == "__main__":
    main()