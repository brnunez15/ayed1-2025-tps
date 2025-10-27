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

def dia_siguiente (dia: int, mes: int, anio: int) -> tuple[int,int,int]:
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

def sumar_dias (fecha: tuple[int, int, int], n: int) -> tuple[int,int,int]:
    """
    Esta funcion suma una cierta cantidad de dias a una fecha correspondiente.

    Pre: La fecha ingresada debe ser valida y la cantidad de dias a sumar debe ser positivo.

    Post: Devuelve una tupla de la fecha ya con los dias sumados.
    """
    dia, mes, anio = fecha

    for _ in range(n):
        dia, mes, anio = dia_siguiente(dia, mes, anio)

    return dia, mes, anio

def validar_horario(horario: tuple[int, int]) -> bool:
    """
    Valida si un horario es valido o no.

    Pre:
        - horario: tupla de dos enteros representando la hora y los minutos.

    Post:
        BOOL
        - True: en caso de que la condicion se cumpla.
        - False: en caso contrario.
    """
    hora, minuto = horario
    return 0 <= hora <= 23 and 0 <= minuto <= 59

def horario_siguiente(horario: tuple[int,int]) -> Tuple[int,int]:
    """
    Cambie el horario ingresado al horario siguiente de un horario valida.

    Pre:
        - horario: hora y minutos ingresados por el usuario.
    
    Post: 
        TUPLA
        - hora: hora incrementada, o no. Dependiendo de la cantidad de minutos.
        - minutos: minuto incrementado.
    """
    hora, minuto = horario
    if minuto < 59:
        minuto += 1
    else:
        minuto = 0
        if hora < 23:
            hora += 1
        else:
            hora = 0
    return hora, minuto


def diferencia_horario(horario1: tuple[int,int], horario2:tuple[int,int]) -> int:
    """
    Muestra la diferencia de minutos que hay entre 2 horarios distintos.

    Pre:
        horario1 (TUPLA): primer horario ingresado por el usuario.
        horario2 (TUPLA): segundo horario ingresado por el usuario.

    Post:
        - contador: este contador es la cantidad de minutos que hay entre horario1 y horario2.
    """
    h1, m1 = horario1
    h2, m2 = horario2

    if (h1, m1) > (h2, m2):
        h1, m1, h2, m2 = h2, m2, h1, m1

    contador = 0

    while (h1, m1) != (h2, m2):
        h1, m1 = horario_siguiente((h1, m1))
        contador += 1

    return contador

def opciones() -> None:
    """
    Imprime las opciones del menu.
    """
    print("Opcion 1: Fechas")
    print("Opcion 2: Horario")
    print("Opcion 0: Salir.")

def menu() -> None:
    """
    Menu principal del programa.
    """
    while True:
        opciones()
        try:
            op = int(input("\nIngrese una opcion: "))
            if op == 0:
                break
            if op == 1:
                while True:
                    print("\n INGRESAR FECHA: \n")
                    try:
                        dia = int(input("Ingrese el dia: "))
                        mes = int(input("Ingrese el mes: "))
                        anio = int(input("Ingrese el anio: "))
                        if validar_fecha((dia, mes, anio)):
                            print(f"\nLa fecha {dia}/{mes}/{anio} es valida")
                            break
                        print(f"\nLa fecha {dia}/{mes}/{anio} es invalida\n")

                    except ValueError as e:
                        print(f"La fecha debe ser un numero entero. {e}\n")
                while True:
                    try:
                        dias = int(input(f"\nIngrese la cantidad de dias que quiera sumar a la fecha {dia}/{mes}/{anio}: "))
                        dia_nuevo, mes_nuevo, anio_nuevo = sumar_dias( (dia, mes, anio), dias)
                        print(f"\nLa fecha luego de agregar {dias} dia/s es: {dia_nuevo}/{mes_nuevo}/{anio_nuevo}\n")
                        break
                    except ValueError as e:
                        print(f"La cantidad de dias debe ser un numero entero. {e}")

            elif op == 2:

                while True:
                    print("\n INGRESAR HORARIO 1 \n")
                    try:
                        hora = int(input("Ingrese la hora: "))
                        minutos = int(input("Ingrese los minutos: "))
                        if validar_horario((hora, minutos)):
                            print(f"\nEl horario {hora}:{minutos} es valido.")
                            break
                        print("El horario ingresado es incorrecto.")
                    except ValueError as e:
                        print(f"El horario debe ser un numero entero. {e}")

                while True:
                    print("\n INGRESAR HORARIO 2 \n")
                    try:
                        hora2 = int(input("Ingrese la hora: "))
                        minutos2 = int(input("Ingrese los minutos: "))
                        if validar_horario((hora2, minutos2)):
                            print(f"\nEl horario {hora2}:{minutos2} es valido.")
                            break
                        print("El horario ingresado es incorrecto.")

                    except ValueError as e:
                        print(f"El horario debe ser un numero entero. {e}")

                diferencia = diferencia_horario((hora, minutos), (hora2, minutos2))

                if diferencia:
                    print(f"\nLa diferencia entre los horarios {hora}:{minutos} y {hora2}:{minutos2} es de: {diferencia} mins\n")
                else:
                    print("No hay diferencia entre los horarios.")
            else:
                print("\nOpcion incorrecta.\n")
        except ValueError as e:
            print(f"La opcion debe ser un entero. {e}")

def main() -> None:
    """
    Funcion principal del programa.
    """
    menu()

if __name__ == "__main__":
    main()