#a_ utilizando solo ciclos normales.
"""
def filtrar_palabras(cadena: str, N: int) -> str:
    lista = list()
    lista_palabras = cadena.split()
    for palabra in lista_palabras:
        if len(palabra) >= N:
            lista.append(palabra)
    resultado = " , ".join(lista)
    return resultado
"""
#b_ utilizando listas po comprension.
"""
def filtrar_palabras(cadena: str, N: int) -> str:
    lista_palabras = cadena.split()
    lista = [palabra for palabra in lista_palabras if len(palabra) >= N]
    resultado = " , ".join(lista)
    return resultado
"""
#c_ utilizando la funcion filter.
def filtrar_palabras(cadena: str, N: int) -> str:
    """
    Filtra las palabras que tengan la misma o mas de la misma longitud que reciba.

    Pre:
        - cadena: recibe la cadena que va a ser filtrada.
        - N: recibe un entero que determina la longitud de filtrado para cada palabra.
    
    Post:
        - resultado: devuelve un string de las palabras que han sido filtradas segun la longitud de N.
    """

    lista_palabras = cadena.split()
    lista = list(filter(lambda palabra: len(palabra) >= N, lista_palabras))
    resultado = " , ".join(lista)
    return resultado

def main() -> None:
    c = input("Ingrese una frase: ")

    try:
        n = int(input("Ingrese un numero: "))
        filtro = filtrar_palabras(c, n)

        if n > 0:
            if not filtro:
                print(f"No hay palabras con {n} o mas caracteres.")
            else:
                print(f"Cadena filtrada con {n} o mas caracteres: '{filtro}'")
        else:
            print("Debes ingresar un numero entero positivo.")

    except ValueError:
        print("Debes ingresar un numero entero.")

if __name__ == "__main__":
    main()