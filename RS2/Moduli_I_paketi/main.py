from shop.proizvodi import *
from shop.narudzbe import *

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

[dodaj_proizvod(Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"])) for proizvod in
 proizvodi_za_dodavanje]

# for proizvod in proizvodi_za_dodavanje:
#    p = Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"])
#    dodaj_proizvod(p)


for proizvod in skladiste:
    p = Proizvod(proizvod["naziv"],proizvod["cijena"],proizvod["dostupna_kolicina"])
    p.ispis()


