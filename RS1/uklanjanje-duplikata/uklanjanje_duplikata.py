def ukloni_duplikate(lista):
    distinkt_lista = list(dict.fromkeys(lista))
    return distinkt_lista

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(ukloni_duplikate(lista))


def ukloni_duplikate_2(lista):
    lista_ured = list(set(lista))
    return lista_ured

lista_2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(ukloni_duplikate_2(lista_2))