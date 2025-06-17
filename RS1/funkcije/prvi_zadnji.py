def prvi_i_zadnji(lista): 
    if len(lista) == 0:
        return None
    else:
        prvi = lista[0]
        zadnji = lista[-1]
        return (prvi, zadnji)
        


lista = [1, 2, 3, 4, 5 ,6 ,7, 8, 9, 10]
print(prvi_i_zadnji(lista))