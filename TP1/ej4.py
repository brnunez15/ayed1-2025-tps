def generar_vuelto(total: int, dinero_recibido: int) -> int:
    """
    Genera el vuelto de una compra distribuido en ciertos billetes.

    Pre: El total y el dinero recibido deben ser números enteros.

    Post: Devuelve la cantidad de billetes correspondientes que debe dar el vuelto.
    """
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    vuelto = dinero_recibido - total

    if vuelto < 0:
        print("El vuelto no se puede entregar debido a la falta de billetes.")

    else:
        if vuelto == 0:
            print("El dinero recibido es justo.")

    for billete in billetes:
        cantidad = vuelto // billete
        if cantidad > 0:
            print(f"{cantidad} billete/s de ${billete}")
            vuelto -= cantidad * billete


def ingresar_total() -> int:
    """
    Permite que el usuario ingrese un número entero en relacion al total de la compra.

    Post: devuelve un número entero (total de la compra).
    """
    total = int(input("Ingresar total de la compra: $"))
    return total

def ingresar_dinero() -> int:
    """Permite que el usuario ingrese un número entero en relacion al dinero que reciba el cajero.
    
    Post: Devuelve un número entero (dinero recibido po el cajero),
    """
    dinero = int(input("Ingresar dinero a pagar: $"))
    return dinero

def main() -> None:
    """Funcion principal del programa.
    """
    total = ingresar_total()
    dinero_recibido = ingresar_dinero()

    generar_vuelto(total, dinero_recibido)

if __name__ == "__main__":
    main()