def prvi_i_zadnji(lista):
    prvi = None
    zadnji = None

    for i, element in enumerate(lista):
        if i == 0:
            prvi = element
        else:
            zadnji = element
    return (prvi, zadnji)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))