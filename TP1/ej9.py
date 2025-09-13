import random as rn
from typing import List

def naranja_peso(naranja:int):
    return [rn.randint(150, 350) for _ in range(naranja)]

def clasificar_naranjas(naranjas: List[int]):
    naranjas_validas = list()
    naranjas_jugo = list()

    for naranja in naranjas:
        if 200 <= naranja <= 300:
            naranjas_validas.append(naranja)
        else:
            naranjas_jugo.append(naranja)

    return naranjas_validas, naranjas_jugo

def llenar_cajones(n_validas):
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

def llenar_camiones(cajones, camion):
    pass

def main():
    cantidad = int(input("Ingrese la cantidad de naranjas: "))
    camion = int(input("Ingrese la cantidad de camiones: "))
    lista_naranjas = naranja_peso(cantidad)
    naranjas_validas, naranjas_jugo = clasificar_naranjas(lista_naranjas)
    
    print(f"Naranjas válidas: {len(naranjas_validas)}")
    print(f"Naranjas para jugo: {len(naranjas_jugo)}\n")

    cajones = llenar_cajones(naranjas_validas)
    for cajon, naranjas in enumerate(cajones):
        print(f"Cajon {cajon + 1}: con {len(naranjas)} naranjas")
    print()
    for cajon, peso in enumerate(cajones):
        print(f"Cajon {cajon + 1}: {sum(peso)}g")


if __name__ == "__main__":
    main()