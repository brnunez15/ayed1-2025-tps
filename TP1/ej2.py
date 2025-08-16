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

def ingresar_fecha () -> int:
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
    Funcion principal del programa
    """
    dia, mes, anio = ingresar_fecha()

    if validar_fecha(dia, mes, anio) == True:
          print(f"La fecha {dia}/{mes}/{anio} es valida")
    else:
        print(f"La fecha {dia}/{mes}/{anio} no es valida")

    if es_bisiesto(anio) == True:
         print(f"El año {anio} es bisiesto")
    
    return None

if __name__ == "__main__":
     main()