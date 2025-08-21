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

def dia_siguiente (dia: int, mes: int, anio: int) -> tuple:
    """
    Esta funcion hace que una fecha ingresada la cambie al dia siguiente de una fecha valida.

    Pre: La fecha ingresada, debe ser una fecha valida.

    Post: devuelve una tupla de la fecha cambiada al dia siguiente.
    """

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

def sumar_dias (dia: int, mes: int, anio: int, n: int) -> tuple:
    """
    Esta funcion suma una cierta cantidad de dias a una fecha correspondiente.

    Pre: La fecha ingresada debe ser valida y la cantidad de dias a sumar debe ser positivo.

    Post: Devuelve una tupla de la fecha ya con los dias sumados.
    """

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

def diferencia_dias(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int) -> int:
    """
    Genera una diferencia de dias entre dos fechas ingresadas.

    Pre: Las fechas ingresadas deben ser validas.

    Post: Devuelve un entero representando la cantidad de dias que hace la diferencia entre las fechas.
    """

    if validar_fecha(d1, m1, a1) == True and validar_fecha(d2, m2, a2) == True:

        if (a1, m1, d1) > (a2, m2, d2):
            d1, m1, a1, d2, m2, a2 = d2, m2, a2, d1, m1, a1

        contador = 0

        while (d1, m1, a1) != (d2, m2, a2):
            d1, m1, a1 = dia_siguiente(d1, m1, a1)
            contador += 1

        return contador

def main () -> None:
    """
    Funcion principal del programa.
    """
    dia, mes, anio = ingresar_fecha()

    if validar_fecha(dia, mes, anio) == True:

        dia_sig, mes_sig, anio_sig = dia_siguiente(dia, mes, anio)

        print(f"El dia siguiente de la fecha ingresada es: {dia_sig}/{mes_sig}/{anio_sig}")

        dias_a_sumar = int(input("Ingrese la cantidad de dias a sumar: "))
        dia_nuevo, mes_nuevo, anio_nuevo = sumar_dias(dia, mes, anio, dias_a_sumar)

        print(f"La fecha luego de agregar {dias_a_sumar} dia/s es: {dia_nuevo}/{mes_nuevo}/{anio_nuevo}\n")

        print("Ingresar dos fechas para saber la diferencia de dias entre ellas: \n")
        dia1, mes1, anio1 = ingresar_fecha()
        print(f"Fecha 1: {dia1}/{mes1}/{anio1}\n")

        dia2, mes2, anio2 = ingresar_fecha()
        print(f"Fecha 2: {dia2}/{mes2}/{anio2}\n")
        
        diferencia_de_dias = diferencia_dias(dia1,mes1,anio1,dia2,mes2,anio)
        
        if diferencia_de_dias > 0:
            print(f"\nLa diferencia de dias entre {dia1}/{mes1}/{anio1} y {dia2}/{mes2}/{anio2} es de: {diferencia_de_dias} dias")
        else:
            print("Las fechas son iguales. No hay diferencia.")
    else:
        print("Debe ingresasar una fecha valida")

if __name__ == "__main__":
    main()