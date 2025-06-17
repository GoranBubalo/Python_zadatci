def filtriraj_parne(lista):
    parna_lista = []
    parna_lista = list(parni for parni in lista if parni % 2 == 0)
    return parna_lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filtriraj_parne(lista))


def filtriraj_parne_2(lista):
    nova_lista = []
    for num in lista:
        if num % 2 == 0:
            nova_lista.append(num)
    return nova_lista
        

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filtriraj_parne_2(lista_2))