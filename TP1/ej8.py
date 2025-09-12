def dia_de_la_semana(dia: int, mes: int, anio: int) -> int:
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    
    siglo = anio // 100
    anio_2 = anio % 100

    dia_sem =  (((26 * mes - 2) // 10) + dia + anio_2 + (anio_2 // 4) + (siglo // 4) - (2 * siglo)) % 7

    if dia_sem < 0:
        dia_sem = dia_sem + 7
    
    return dia_sem

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
    
    if mes in  (1, 3, 5, 7, 8, 10, 12):
        return 1 <= dia <= 31

    elif mes in (4, 6, 9, 11):
        return 1 <= dia <= 30

    if mes == 2:
        if es_bisiesto(anio):  
            return 1 <= dia <= 29

        else:
             return 1 <= dia <= 28


def es_bisiesto (anio: int) -> bool:
     """
     Verifica si un año ingresado es bisiesto, o no.

     Pre: El número ingresado tiene que ser un entero positivo.

     Post: Retornará (True) si el año es bisiesto. Por lo contrario retorna (False).
     """
     return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

def dias_mes (mes: int, anio: int) -> int:
    """
    Calcula la cantidad de dias que tiene un mes especifico en un año dado.

    Pre: recibe un numero entero representando el mes y otro entero representando el año.

    Post: retorna un entero representando la cantidad de dias correspondientes a cada mes.
    """
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif es_bisiesto(anio):
        return 29
    else:
        return 28
    
def arma_mes(dia: int, dias: int) -> list[int]:
    """
    Genera una lista con los dias de un mes segun el dia de la semana en el que comienza este.

    Pre: recibe un entero en representacion a un dia de la semana. Luego recibe 
    un numero entero positivo que indica la cantidad total de dias del mes.

    Post: devuelve la lista con la cantidad de 0 que representan los dias vacios al inicio de la semana
    y los demas son numeros del 1 hasta todos los dias de determinado mes.
    """
    lista_mes = [0 for _ in range(dia) if dia]
    for d in range(1, dias + 1):
        lista_mes.append(d)
    return lista_mes

def imprimir_calendario(lista_mes: list[int], mes: int, anio: int) -> None:
    """
    Imprime el calendario de un mes recibido, alineando los dias segun la semana.

    Pre: Recibe una lista de enteros que representa los dias del mes, con ceros al inicio.
    Luego recibe un numero entero representando al mes ingresado por el usuario.
    Y por ultimo un numero entero representando al año ingresado por el usuario

    Post: Imprime el calendario completo del mes correspondiente. 
    No retorna ningun valor (None).
    """
    print(f"\n-- {meses[mes - 1]} de {anio} --")
    print(" ".join(dias))

    semanas = [lista_mes[i:i+7] for i in range(0, len(lista_mes), 7)]

    for semana in semanas:
        for d in semana:
            if d:
                print(f"{d:>2}", end='  ')
            else:
                print(f"{'':>2}", end='  ')
        print()
    return None
        

def main() -> None:
    while True:
        mes = int(input("Ingrese el número de un mes (1-12): "))
        anio = int(input("Ingrese un año (1900-2025): "))

        if validar_fecha(1, mes, anio):
            break

        print("Fecha inválida.")

    dias = dias_mes(mes, anio)
    primer_dia_sem = dia_de_la_semana(1, mes, anio)
    lista_mes = arma_mes(primer_dia_sem, dias)
    imprimir_calendario(lista_mes, mes, anio)

dias = ("Dom", "Lun", "Mar", "Mier", "Jue", "Vier", "Sab")
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

if __name__ == "__main__":
    main()