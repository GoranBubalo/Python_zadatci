class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def __repr__(self):
        return (f"naziv = {self.naziv}, \n"
                f"cijena =  {self.cijena}, \n"
                f"dostupna_kolicina =  {self.dostupna_kolicina}")

    def ispis(self):
        print(f"naziv : {self.naziv},cijena : {self.cijena}, dostupna_kolicina : {self.dostupna_kolicina} ")


cokolada = Proizvod("Milka", "3.20", 23)
pice = Proizvod("Coca-cola", "3.50", 15)
skladiste = [{"naziv": cokolada.naziv, "cijena": cokolada.cijena, "dostupna_kolicina": cokolada.dostupna_kolicina},
             {"naziv": pice.naziv, "cijena": pice.cijena, "dostupna_kolicina": pice.dostupna_kolicina}]


def dodaj_proizvod(proizvod):
    skladiste.append({
        "naziv": proizvod.naziv,
        "cijena": proizvod.cijena,
        "dostupna_kolicina": proizvod.dostupna_kolicina
    })
