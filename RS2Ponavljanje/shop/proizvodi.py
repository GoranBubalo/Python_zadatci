class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} kn, Količina: {self.kolicina}")

    def ukupna_cijena(self):
        return self.cijena * self.kolicina
    

listu_skladiste = [
    Proizvod("Laptop", 5000, 10),
    Proizvod("Telefon", 3000, 20),
    Proizvod("Tablet", 2000, 15),
    Proizvod("Monitor", 1500, 5),
    Proizvod("Tipkovnica", 300, 50)
]

def dodaj_proizvod(naziv, cijena, kolicina):
    novi_proizvod = Proizvod(naziv, cijena, kolicina)
    listu_skladiste.append(novi_proizvod)