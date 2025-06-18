import random

random_broj = random.randint(1, 100)
broj_pokusaja = 0

while True:
    pokusaj = input("Pogodi broj između 1 i 100: ")
    
    if not pokusaj.isdigit():
        print("Molimo unesite valjani broj.")
        continue
    
    pokusaj = int(pokusaj)
    broj_pokusaja += 1
    
    if pokusaj < random_broj:
        print("Broj je veći.")
    elif pokusaj > random_broj:
        print("Broj je manji.")
    else:
        print(f"Čestitamo! Pogodili ste broj {random_broj} u {broj_pokusaja} pokušaja.")
        break