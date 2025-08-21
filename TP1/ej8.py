def dia_de_la_semana(dia: int, mes: int, anio: int):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    
    siglo = anio // 100
    anio_2 = anio % 100

    dia_sem =  (((26 * mes - 2) // 10) + dia + anio_2 + (anio_2 // 4) + (siglo // 4) - (2 * siglo)) % 7

    if dia_sem < 0:
        dia_sem = dia_sem + 7
    
    return dia_sem

print(dia_de_la_semana(15, 10, 2025))