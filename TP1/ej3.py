def total_gastos(cant_viajes: int) -> float:
    """
    Calcula el total de gastos que debe cubrir en un mes.

    Pre: La cantidad de viajes debe ser mayor a 0.

    Post: Devuelve el total de gastos en viajes segun el porcentaje correspondiente.
    """

    TARIFA_MAXIMA = 996

    if cant_viajes >= 1 and cant_viajes <= 20:
        return TARIFA_MAXIMA * cant_viajes
    
    elif cant_viajes >= 21 and cant_viajes <= 30:
        return TARIFA_MAXIMA * 0.8 * cant_viajes
    
    elif cant_viajes >= 31 and cant_viajes <= 40:
        return TARIFA_MAXIMA * 0.7 * cant_viajes
    
    else:
        return TARIFA_MAXIMA * 0.6 * cant_viajes
    
def ingresar_cant_viajes () -> int:
    """
    Permite ingresar la cantidad de viajes realizados en un mes.

    Post: Devuelve un entero que representa la cantidad de viajes ingresada por el usuario.

    """
    cant_viajes = int(input("Ingresa la cantidad de viajes que realizaste en un mes: "))
    return cant_viajes

def main() -> None:
    """
    Función principal del programa.
    """
    viajes = ingresar_cant_viajes()
    if viajes > 0:
        print(f"El total de gastos que debe cubrir es de: {total_gastos(viajes):.2f}")
    else:
        print("Debe ingresar al menos un viaje")

if __name__ == "__main__":
    main()