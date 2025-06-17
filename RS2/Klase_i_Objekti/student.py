class Student:
    ime = ""
    prezime = ""
    godine = 0
    ocijene = []

    def __init__(self,ime,prezime,godine,ocijene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocijene = ocijene

    def __repr__(self):
        return f"{self.ime} {self.prezime} {self.godine} {self.ocijene}"

    def prosijek(self):
        return sum(self.ocijene) / len(self.ocijene)


studenti = [
 {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
 {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
 {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
 {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
 {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
 {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = {
    student["ime"] : Student(student["ime"],student["prezime"],student["godine"],student["ocjene"])
    for student in studenti
}

# Student sa najboljim prosijekom
najbolji_student = max(studenti_objekti.values(), key=lambda student : student.prosijek())

print(najbolji_student)
print(studenti_objekti)

