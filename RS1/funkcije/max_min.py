def maks_i_min(lista):
    if not lista:
        return None

    najveci = lista[0]
    najmanji = lista[0]

    for broj in lista:
        if broj > najveci:
            najveci = broj
        elif broj < najmanji:
            najmanji = broj
    return [najmanji, najveci]


lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista)) 