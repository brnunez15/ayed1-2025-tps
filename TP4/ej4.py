import random as rn
from random import randint

def gen_numeros() -> int:
    """
    Genera un numero aleatorio entre 0 y 3999.

    Post:
        devuelve un numero aleatorio.
    """
    return rn.randint(0, 3999)

def pasar_a_romano(num: int) -> str:
    """
    Pasa un numero entero a un numero romano.

    Pre:
        num: recibe el entero que va a ser transformado.

    Post:
        numero_r: retorna un string representando al numero romano correspondiente al numero recibido.
    """
    valores = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
        ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4),
        ("I", 1)
    ]

    numero_r = ""

    for s, v in valores:
        while num >= v:
            numero_r += s
            num -= v

    return numero_r
        
def main() -> None:
    numero = gen_numeros()
    romano = pasar_a_romano(numero)

    print(f"Numero entero: {numero}")
    print(f"Numero romano: {romano}")

if __name__ == "__main__":
    main()