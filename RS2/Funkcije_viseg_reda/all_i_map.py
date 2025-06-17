studenti = [
 {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
 {"ime": "Marko", "prezime": "Marković", "godine": 22},
 {"ime": "Ana", "prezime": "Anić", "godine": 21},
 {"ime": "Petra", "prezime": "Petrić", "godine": 19},
 {"ime": "Iva", "prezime": "Ivić", "godine": 19},
 {"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda student: student["godine"] >=18, studenti))
print(svi_punoljetni) # False