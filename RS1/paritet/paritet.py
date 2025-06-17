def grupiraj_po_paritetu(lista):

    dict = {"parni" : [], "neparni" : []}

    # looping tehnika
    for i in lista:
        if i % 2 == 0:
            dict["parni"].append(i)
        elif i % 2 !=0:
            dict["neparni"].append(i)
    
    return dict


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))