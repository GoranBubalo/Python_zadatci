skriveni_broj = 4
broj_pokusaja = 0
broj_je_pogoden = False

while broj_je_pogoden is False: 

    korisnik_broj = int(input("Pogodi skriveni brroj: "))

    if korisnik_broj < skriveni_broj:
        print("Uneseni broj je manji")
        broj_pokusaja += 1
    elif korisnik_broj > skriveni_broj:
        print("Uneseni broj je veći")
        broj_pokusaja += 1
    elif korisnik_broj == skriveni_broj:
        print(f"Bravo pogodio si u {broj_pokusaja} pokusaja")
        broj_je_pogoden = True