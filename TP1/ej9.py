import random as rn
from typing import List, Tuple

def naranja_peso(naranja:int) -> List[int]:
    """
    Genera una lista con numeros aleatorios representando el peso de cada naranja ingresada.

    Pre: recibe un entero representando la cantidad de naranjas ingresadas por el usuario.

    Post: devuelve una lista con los pesos de cada una de las naranjas.
    """
    return [rn.randint(150, 350) for _ in range(naranja)]

def clasificar_naranjas(naranjas: List[int]) -> Tuple[list[int], list[int]]:
    """
    Clasifica las naranjas segun su respectivo peso y condiciones.

    Pre: recibe una lista de naranjas con sus pesos.

    Post: devuelve una tupla con una lista de naranjas validas y otra de naranjas para jugo.
    """
    naranjas_validas = list()
    naranjas_jugo = list()

    for naranja in naranjas:
        if 200 <= naranja <= 300:
            naranjas_validas.append(naranja)
        else:
            naranjas_jugo.append(naranja)

    return naranjas_validas, naranjas_jugo

def llenar_cajones(n_validas: list[int]) -> List[list[int]]:
    """
    Se encarga de llenar cajones de naranjas siguiendo las condiciones.

    Pre: recibe una lista de naranjas validas para llenar al cajon.

    Post: devuelve una matriz, donde cada lista representa un cajon de hasta 100 naranjas.
    """
    cajones = list()
    cajon_actual = list()

    for naranja in n_validas:
        cajon_actual.append(naranja)
        if len(cajon_actual) == 100:
            cajones.append(cajon_actual)
            cajon_actual = []

    if cajon_actual:
        cajones.append(cajon_actual)
    
    return cajones

def llenar_camiones(cajones: List[List[int]], camiones: int) -> Tuple[List[int], int]:
    """
    Distribuye los cajones de naranjas en camiones respetando los limites de peso.
    
    Pre: recibe una lista de listas, cada sublista contiene los pesos de las naranjas de un cajon.
    Luego recibe un entero representando la cantidad de camiones disponibles ingresadas por el usuario.

    Post: retorna una tupla con una lista con los pesos de los camiones despachados (en gramos).
    Luego un entero con el peso sobrante (tambien en gramos).
    """
    capacidad_max = 500000
    capacidad_min = 400000

    camiones_despachados = list()
    camion_actual = list()
    peso_actual = 0
    sobrantes = list()

    for cajon in cajones:
        peso_cajon = sum(cajon)
        if peso_actual + peso_cajon <= capacidad_max:
            camion_actual.append(cajon)
            peso_actual += peso_cajon
        else:
            if peso_actual >= capacidad_min:
                camiones_despachados.append(camion_actual.copy())
            else:
                sobrantes.extend(camion_actual)
            camion_actual = [cajon]
            peso_actual = peso_cajon

            if len(camiones_despachados) >= camiones:
                sobrantes.extend(camion_actual)
                camion_actual = list()
                peso_actual = 0

    if camion_actual:
        if peso_actual >= capacidad_min and len(camiones_despachados) < camiones:
            camiones_despachados.append(camion_actual.copy())
        else:
            sobrantes.extend(camion_actual)

    return camiones_despachados, sobrantes
        
def main() -> None:
    cantidad = int(input("Ingrese la cantidad de naranjas: "))
    camiones = int(input("Ingrese la cantidad de camiones: "))
    lista_naranjas = naranja_peso(cantidad)
    naranjas_validas, naranjas_jugo = clasificar_naranjas(lista_naranjas)
    
    print(f"Naranjas válidas: {len(naranjas_validas)}")
    print(f"Naranjas para jugo: {len(naranjas_jugo)}\n")

    cajones = llenar_cajones(naranjas_validas)
    for cajon, naranjas in enumerate(cajones):
        print(f"Cajon {cajon + 1}: con {len(naranjas)} naranjas")
    print()

    for i, cajon in enumerate(cajones):
        print(f"Cajón {i+1}: {len(cajon)} naranjas, {sum(cajon)}g")
    print()
    
    camiones_dispo, sobrante = llenar_camiones(cajones, camiones)

    for i, camion in enumerate(camiones_dispo):
        peso_camion = sum(sum(c) for c in camion)
        print(f"Camión {i+1}: {len(camion)} cajones, peso {peso_camion} g")

    if sobrante:
        peso_sobrante = sum(sum(c) for c in sobrante)
        print(f"\nCajones sobrantes: {len(sobrante)}")
        print(f"Peso sobrante: {peso_sobrante} g")
    else:
        print("\nNo hay sobrantes.")

if __name__ == "__main__":
    main()