import re
from typing import List, Tuple

def registrar_socios (numero_socio: int, lista_socios: list[int]) -> List[int]:
    """
    Registra socios y los agrega a una lista.

    Pre: recibe el numero del socio y una lista global para agregar estos mismos.

    Post: Devuelve una lista son los numeros de socios registrados.
    """

    patron_socio = re.compile(r"\d{5}")

    if not patron_socio.fullmatch(str(numero_socio)):
        return None
    
    else:
        lista_socios.append(numero_socio)
        return lista_socios
    
def cantidad_ingresos(socios: List[int]) -> List[Tuple[int, int]]:
    """
    Muestra la cantidad de ingresos de todos los socios registrados.

    Pre: Recibe la lista con todos los socios.

    Post: Devuelve una lista de una tupla de los socios y su respectiva cantidad de ingresos.
    """
    ingresos = list()
    
    for socio in set(socios):
        cant_ingresos = socios.count(socio)
        ingresos.append((socio, cant_ingresos))

    return ingresos

def eliminar_socio(numero_socio: int, socios: list[int]) -> Tuple[List[int], int]:
    """
    Elimina todas las veces que un socio ingreso al club.

    Pre: Recibe el numero de socio que sera eliminado, y la lista de todos los socios para verificar si esta.

    Post: Devuelve una tupla de la lista con el/los socios eliminados y la cantidad de veces que se elimino el mismo.
    """
    lista_eliminados = list()

    while numero_socio in socios:
            socios.remove(numero_socio)
            lista_eliminados.append(numero_socio)
            veces_eliminadas = lista_eliminados.count(numero_socio)

    return lista_eliminados, veces_eliminadas

def opciones() -> None:
    print("Opcion 1: Registrate en el club.")
    print("Opcion 2: Ver listado de socios en el club.")
    print("Opcion 3: Ver cuantas veces ingreso al club cada socio.")
    print("Opcion 4: Dar de baja un socio.")
    print("Opcion 0: Para salir.")

def menu() -> None:
    """
    Función que muestra el menu principal del sistema de registro de socios.
    """
    lista_socios = list()
    
    while True:
        opciones()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 0:
            print("Saliendo...")
            break

        elif opcion == 1:

            while True:
                socio = int(input("Ingrese su numero de socio: / 0: salir: "))
            
                if socio == 0:
                    break
                registrar = registrar_socios(socio, lista_socios)

                if registrar == None:
                    print("Debe ingresar un numero de 5 digitos.")
                    
                else:
                    print(f"Socio {socio} ha sido registrado correctamente.")

            
        elif opcion == 2:

            while True:
                if lista_socios:
                    print(f"Listado de socios registrados: {list(set(lista_socios))}")
                else:
                    print("Aun no hay socios registrados en el club.")

                salir = int(input("Ingrese 0 para volver al menu: "))

                if salir == 0:
                    break
        
        elif opcion == 3:

            while True:

                resumen = cantidad_ingresos(lista_socios)
                if resumen:
                    for numero_socio, cantidad in resumen:
                        print(f"{numero_socio} ha ingresado {cantidad} veces/vez")
                else:
                    print("Aun no hay socios registrados en el club.")
                
                salir = int(input("Ingrese 0 para volver al menu: "))
                if salir == 0:
                    break

        elif opcion == 4:

            while True:

                if lista_socios:
                    print(f"Registro de entradadas de los socios: {list(set(lista_socios))}")

                    n_socio = int(input("Ingrese un socio para eliminar: "))
                    if n_socio in lista_socios:

                        eliminados, veces = eliminar_socio(n_socio, lista_socios)

                        if veces > 0:
                            print(f"Socio eliminado: {list(set(eliminados))}")
                            print(f"Se eliminaron {veces} ingresos del socio {n_socio}")
                            if lista_socios:
                                print(f"Lista de socios luego de haber eliminado: {lista_socios}")
                            else:
                                print("No hay socios registrados")
                        else:
                            print(f"El socio {n_socio} no ha sido registrado.")
                    else:
                        print("Debe ingresar un numero de socio valido.")
                else:
                    print("Aun no hay socios registrados en el club.")
                    
                salir = int(input("Ingrese 0 para volver al menu: "))
                if salir == 0:
                    break
        else:
            print("\nOpcion incorrecta\n")
def main() -> None:
    menu()        

if __name__ == "__main__":
    main()        