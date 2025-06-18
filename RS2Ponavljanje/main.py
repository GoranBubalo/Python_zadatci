from shop import proizvodi

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])
    
for proizvod in proizvodi.listu_skladiste:
    proizvod.ispis()
    print(f"Ukupna cijena za {proizvod.naziv}: {proizvod.ukupna_cijena()} kn")