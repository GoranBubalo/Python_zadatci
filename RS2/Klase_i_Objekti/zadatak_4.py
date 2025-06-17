import datetime

from sympy.physics.units import years


class Automobil:
    marka = ""
    model = "Blank"
    godina_proizvodnje = 0
    kilometraža = 0

    def __init__(self, marka, model, godina_proizvodnje,kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža

    def ispis(self):
        return (f"marka automobila je {self.marka}\n"
              f"model automobila je {self.model}\n"
              f"godina proizvodnje automobila je {self.godina_proizvodnje}\n"
              f"kilometraža automobila je {self.kilometraža}")

    def staros(self):
        print (f"automobil je star {datetime.datetime.now().year - self.godina_proizvodnje }\n")

automobil = Automobil("Mercedes","A1",2015,50000)

print(automobil.ispis())
automobil.staros()
