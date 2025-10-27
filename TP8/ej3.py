import re
from typing import Tuple

def sin_caracteres(mail: str) -> Tuple:
    """
    Separa las partes de una direccion de mail valida.

    Pre:
        - mail: recibe un mail el cual va a ser dividido segun sus partes.
    
    Post:
        - resultado: Devuelve una tupla con las partes de la direccion del mail divididas.
            si el mail es invalido, devuelve una tupla vacia.
    """
    patron = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
    resultado = ()
    coincidencia = re.match(patron, mail)

    if coincidencia:
        usuario, dominio = mail.split("@")
        partes_dominio = dominio.split(".")
        resultado = tuple([usuario] + partes_dominio)
    return resultado

def main() -> None:
    """
    Funcion principal del programa.
    """
    cadena = input("Ingrese su usuario de mail: ")
    sin_ch = sin_caracteres(cadena)
    if sin_ch:
        print(f"Partes que componen su direccion de mail: {sin_ch}")
    else:
        print(f"{sin_ch}. Su mail es invalido")

if __name__ == "__main__":
    main()