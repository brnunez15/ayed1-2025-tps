def GrabarRangoAlturas(atletas, deportes, alturas, deportes_dict):
    try:
        with open('TP6/EJ3/alturas.txt', 'wt', encoding='utf-8') as arch:
            for codigo, nombre_deporte in deportes_dict.items():
                arch.write(f"Deporte: {nombre_deporte}\n")
                for i, atleta in enumerate(atletas):
                    if deportes[i] == codigo:
                        arch.write(f"Altura: {alturas[i]} cm - Atleta: {atleta}\n")
    except FileNotFoundError as e:
        print(e)

def main():
    lista_atletas = []
    lista_deportes = []
    lista_alturas = []
    deportes = {"1": "Basquet",
                "2": "Futbol",
                "3": "Natacion"}

    while True:
        atleta = input("Ingrese su nombre (ENTER para salir): ")
        if atleta == "":
            break
        lista_atletas.append(atleta)

        print("\n----DEPORTES----\n")
        for clave, valor in deportes.items():
            print(f"{clave}: {valor}")

        deporte = input("\nIngrese un deporte: ")
        lista_deportes.append(deporte)

        altura = int(input("Ingrese su altura: "))
        lista_alturas.append(altura)
    GrabarRangoAlturas(lista_atletas, lista_deportes, lista_alturas, deportes)

if __name__ == "__main__":
    main()