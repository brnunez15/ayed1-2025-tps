from typing import List, Tuple

def leer_archivo() -> List[str]:
    """
    Lee un archivo txt y todas las lineas las agrega a una lista.

    Post:
        - lineas: devuelve la lista con todas las lineas de texto del archivo leido.
    """
    try:
        lineas = []
        with open ('TP6/EJ1/ej1.txt', 'rt', encoding='utf-8-sig') as arch:
            while True:
                linea = arch.readline()
                if not linea:
                    break
                lineas.append(linea.strip())
    except FileNotFoundError as e:
        print(f'No se encuentra el archivo: {e}')
    return lineas

def clasificar_apellidos(lineas: list[str]) -> Tuple[list[str], list[str], list[str]]:
    """
    Clasifica los apellidos segun la condicion especificada.
    Aquellos que terminen en 'INI' deberan ser guardados en la lista italia.
    Aquellos que terminen en 'IAN' deberan ser guardados en la lista armenia.
    Aquellos que terminen en 'EZ' deberan ser guardados en la lista espania.

    Pre:
        -lineas: recibe la lista con todas las lineas de texto (nombres) del archivo abierto previamente.

    Post:
        TUPLA:
        - italia: lista con todos los nombres y los apellidos que terminan con 'INI'.
        - armenia: lista con todos los nombres y los apellidos que terminan con 'IAN'.
        - espania: lista con todos los nombres y los apellidos que terminan con 'EZ'.
    """
    italia = []
    armenia = []
    espania = []
    for linea in lineas:
        nombres = linea.split(',')
        apellido = nombres[0].strip().upper()
        nombre = nombres[1].strip().upper()
        if apellido[-3:] == "INI":
            italia.append(f"{apellido}, {nombre}")
        elif apellido[-3:] == "IAN":
            armenia.append(f"{apellido}, {nombre}")
        elif apellido[-2:] == "EZ":
            espania.append(f"{apellido}, {nombre}")
    return italia, armenia, espania

def crear_archivos(italia: list[str], armenia: list[str], espania: list[str]) -> None:
    """
    Crea los archivos de los paises correspondientes si es que no existian.
    Y guarda los nombres y apellidos en cada archivo segun su condicion.

    Pre:
        - italia: lista de los nombres con apellido terminado en 'INI'.
        - armenia: lista de los nombres con apellido terminado en 'IAN'.
        - espania: lista de los nombres con apellido terminado en 'EZ'.
    """
    try:
        with open('TP6/EJ1/ARMENIA.TXT', 'wt', encoding='utf-8-sig') as ar:
            ar.write("\n".join(armenia))
        with open('TP6/EJ1/ITALIA.TXT', 'wt', encoding='utf-8-sig') as it:
            it.write("\n".join(italia))
        with open('TP6/EJ1/ESPAÑA.TXT', 'wt', encoding='utf-8-sig') as esp:
            esp.write("\n".join(espania))
    except FileNotFoundError as e:
        print(f'No se encuentra el archivo: {e}')

def main() -> None:
    """
    Funcion principal del programa.
    """
    lineas = leer_archivo()
    print(lineas)
    it, arm, esp = clasificar_apellidos(lineas)
    crear_archivos(it,arm,esp)
    print("Se realizo bien todo")
if __name__ == "__main__":
    main()