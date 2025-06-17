class Radnik:
    ime = ""
    porzicija = ""
    placa = 0

    def __init__(self, ime, porzicija, placa):
        self.ime = ime
        self.porzicija = porzicija
        self.placa = placa

    def work(self):
        return f"Radim na poziciji {self.porzicija}"

class Manager(Radnik):
    department = ""

    def __init__(self, department, ime, pozicija, placa):
        super().__init__(ime,pozicija,placa)
        self.department = department


    def work(self):
        return f"{super().work()} u odjelu {self.department}"

    def give_raise(self,radnik, povecanje):
        return f"Radnik {radnik.ime} je dobio povećanje za iznos {povecanje}"

ivan = Radnik("Ivan", "Junior Dev", 1200)
it = Manager("IT odjel","Ana","Seinor Dev", 2300)
print(it.work())
print(it.give_raise(ivan,200))
