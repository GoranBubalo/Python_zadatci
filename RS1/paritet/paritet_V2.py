def grupiraj_po_paritetu(lista):

    # List comprehesion metoda 
    parni = [i for i in lista if i % 2 == 0]
    neparni = [i for i in lista if i % 2 != 0] 

    return {'parni' : parni, 'eparni' : neparni}


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))