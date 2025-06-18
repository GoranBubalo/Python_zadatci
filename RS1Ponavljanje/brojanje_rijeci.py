tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

# {'Python': 2, 'je': 3, 'programski': 1, 'jezik': 1, 'koji': 1, 'jednostavan': 1, 'za': 1, 'učenje': 1, 'i': 1, 'korištenje.': 1, 'vrlo': 1, 'popularan.': 1}

def brojanje_riječi(tekst):
    riječi = tekst.split()
    broj_riječi = {}
    
    for riječ in riječi:
        riječ = riječ.strip('.,!?;:')  # Uklanjanje interpunkcijskih znakova
        if riječ in broj_riječi:
            broj_riječi[riječ] += 1
        else:
            broj_riječi[riječ] = 1
            
    return broj_riječi

print(brojanje_riječi(tekst))

