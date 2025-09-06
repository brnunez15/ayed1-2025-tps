import re
from typing import Tuple

def registro_pacientes(num_afiliado: int, estado_consulta: int, turnos: list[int], urgencias: list[int]) -> Tuple[list[int], list[int]] | None:
    """
    Registra pacientes segun el estado de consulta que tenga el mismo.

    Pre: Recibe un numero de afiliado del paciente, el estado de consula, y las listas del tipo de consulta (por turno o por urgencia)

    Post: Devuelve una tupla de las listas con el numero de afiliado del paciente segun se haya registrado por el estado de consulta.
    """

    patron_afiliado = re.compile(r"\d{4}")

    if not patron_afiliado.fullmatch(str(num_afiliado)):
        return None
    
    else:
        if estado_consulta == 1:
            turnos.append(num_afiliado)
            
        elif estado_consulta == 0:
                urgencias.append(num_afiliado)
        
    return turnos, urgencias

def cantidad_asistencias (turnos: list[int], urgencias: list[int], num_afiliado: int) -> Tuple[int, int]:
    """
    Registra la cantidad de veces que un paciente se registro en una consuta (por turno o por urgencia)

    Pre: Recibe la lista de turno y la de urgencias. A su vez tambien recibe el numero de afiliado.

    Post: Devuelve una tupla de la cantidad de veces que el afiliado recibido se registro en turnos y en urgencias.
    """

    cant_turnos = turnos.count(num_afiliado)    
    cant_urgencias = urgencias.count(num_afiliado)

    return cant_turnos, cant_urgencias

def opciones() -> None:
    """
    Imprime las opciones del menu.
    """
    print("Opcion 1: Registrarse a una consulta")
    print("Opcion 2: Ver listado de asistencias")
    print("Opcion 3: Buscar por paciente, cuantas veces se atendio por turno y cuantas por urgencia.")
    print("Opcion 0: Salir")

def menu() -> None:
    """
    Función que muestra el menu principal del sistema de registro de pacientes.
    """
    lista_turnos = list()
    lista_urgencias = list()
    
    while True:

        opciones()
        opcion = int(input("Ingrece una opcion: "))

        if opcion == 0:
            print("Saliendo...")
            break

        if opcion == 1:

            while True:

                n_afiliado = int(input("Ingrese un numero de afiliado: "))
                consulta = int(input("Ingrese su estado de consulta. 1: turno, 0: urgencia, -1: salir: "))

                if consulta == -1:
                    break

                registro = registro_pacientes(n_afiliado, consulta, lista_turnos, lista_urgencias)

                if registro == None:
                    print("Debe ingresar un numero de 4 digitos.")
                
            
        elif opcion == 2:
                
                if len(lista_turnos) > 0:
                    print(f"Pacientes atendidos por turno: {lista_turnos}")
                else:
                    print("No hay pacientes asistidos por turno.")
                
                if len(lista_urgencias) > 0:
                    print(f"Pacientes atendidos por urgencia: {lista_urgencias}")
                else:
                    print("No hay pacientes asistidos por urgencia.")

        elif opcion == 3:

            while True:

                n_afiliado = int(input("Buscar paciente por numero de afiliado: / -1: salir: "))

                if n_afiliado == -1:
                    break

                cantidad_turnos, cantidad_urgencias = cantidad_asistencias(lista_turnos, lista_urgencias, n_afiliado)

                if cantidad_turnos == 0 and cantidad_urgencias == 0:
                    print(f"{n_afiliado} no está registrado en la clínica.")
                
                else:
                    if cantidad_urgencias > 0:
                        print(f"La cantidad de veces que {n_afiliado} se atendio por urgencia: {cantidad_urgencias}")
                    else:
                        print(f"{n_afiliado} no ha sido atendido por urgencia")
                
                
                    if cantidad_turnos > 0:
                        print(f"La cantidad de veces que {n_afiliado} se atendio por turno: {cantidad_turnos}")
                    else:
                        print(f"{n_afiliado} no ha sido atendido por turno.")

def main() -> None:
    menu()

if __name__ == "__main__":
    main()