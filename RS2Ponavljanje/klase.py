from datetime import datetime

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

class Automobil: 
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}, Kilometraža: {self.kilometraza} km")
        
    def starost(self): 
        starost_auta = datetime.now().year - self.godina_proizvodnje
        return starost_auta
        
        
auto = Automobil("Toyota", "Corolla", 2020, 15000)
auto.ispis()  # Output: Marka: Toyota, Model: Corolla, Godina proizvodnje: 2020, Kilometraža: 15000 km

print(f"Auto je staro {auto.starost()}. godina")  # Output: 3 (ako je trenutna godina 2023)

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def množenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno"
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        if self.a >= 0:
            return self.a ** 0.5
        else:
            return "Korijen negativnog broja nije definiran"
        
        
class Student: 
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    
    def prosjek_ocjena(self):
        if self.ocjene:
            return sum(self.ocjene) / len(self.ocjene)
        else:
            return 0
    

studenti_objekti = []
for student in studenti:
    novi_student = Student(student["ime"], student["prezime"], student["godine"], student["ocjene"])
    studenti_objekti.append(novi_student)

najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek_ocjena())
print(f"Najbolji student je {najbolji_student.ime} {najbolji_student.prezime} s prosjekom ocjena {najbolji_student.prosjek_ocjena():.2f}.")  # Output: Ana Anić s prosjekom ocjena 5.00.