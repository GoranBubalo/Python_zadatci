import asyncio
import time

# Baza podataka korisnika i lozinke
baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


# Autentifikacija korisnika
async def autentifikacija(korisnik):
    print("Simulacija provjere korisnickog imena")
    await asyncio.sleep(3)

    for kor in baza_korisnika:
        if kor['korisnicko_ime'] == korisnik['korisnicko_ime'] and kor['email'] == korisnik['email']:
            return await autorizacija(kor,korisnik['lozinka'])

    return f"Korisnik {korisnik} nije pronađen"


# Autorizacija
async def autorizacija(korisnik_iz_baze, lozinka):
    print("Simulacija dekripcija lozinke i provjeru s lozinkom iz baze lozinka")
    await asyncio.sleep(2)

    # Provjera lozinke u bazi
    for loz in baza_lozinka:
        if loz['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime'] and loz['lozinka'] == lozinka:
            return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija uspješna."

    return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija neuspješna."


async def main():
    start = time.time()
    korisnici = [
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com', 'lozinka': 's324SDFfdsj234'},
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'pogresna_lozinka'}
    ]

    tasks = [autentifikacija(korisnik) for korisnik in korisnici]
    rezultati = await asyncio.gather(*tasks)

    for rezultat in rezultati:
        print(rezultat)
    end = time.time()
    print(end-start)


# Pokretanje programa
asyncio.run(main())
