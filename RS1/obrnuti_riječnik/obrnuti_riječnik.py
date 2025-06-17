def obrni_rijecnik(rijecnik):
    obrnuti_rijecnik = {}
    for keys, value in rijecnik.items():
          obrnuti_rijecnik[value] = keys
    return obrnuti_rijecnik


rijecnik = {"ime" : "Ivan", "prezime" : "Ivić", "dob" : 25}
print(obrni_rijecnik(rijecnik))