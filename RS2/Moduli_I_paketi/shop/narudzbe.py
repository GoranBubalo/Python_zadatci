from proizvodi import *

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

def napravi_narudzbu(lista_proizvoda):

    if not isinstance(lista_proizvoda, list):
        return "argument lista_proizvoda nije tipa lista"

    if not all(isinstance(element,dict) for element in lista_proizvoda):
        return "Nisu svi elementi u listi rječnik"

    #TODO:: Obavezni ključevi ==> Vraća samo prvi proizvod koji nema druge niti ne gleda treba popraviti
    obavezni_kljucevi = {'naziv', 'cijena', 'narucena_kolicina'}
    for proizvoda in lista_proizvoda:
        if not  obavezni_kljucevi.issubset(proizvoda.keys()):
            return f"Proizvod {proizvoda} ne sadrži sve obvezne ključeve : {obavezni_kljucevi}"

    if not lista_proizvoda:
        return "Lista ne smije biti prazna"

    ukupna_cijena = sum(
        proizvoda['naruceni_proizvodi'] * proizvoda['cijena'] for proizvoda in lista_proizvoda
    )

    for proizvod in lista_proizvoda:
        if proizvod["dostupna_kolicina"] <=0:
            return (f"Proizvod {proizvod['naziv']} nije dostupan")
    return "Proizvodi su dostupni"


print(napravi_narudzbu(skladiste))