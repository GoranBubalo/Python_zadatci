import asyncio
import time

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


async def autentifikacija(korisnik):
    await asyncio.sleep(3)

    for kor in baza_korisnika:
        if kor['korisnicko_ime'] == korisnik['korisnicko_ime'] and kor['email'] == korisnik['email']:
            return autorizacija(kor, korisnik['lozinka'])

    return f"Korisnik {korisnik} nije pronađen"


async def autorizacija(korisnik, baza_lozinka):
    await asyncio.sleep(2)

    for lz in baza_lozinka:
        if lz['korisnicko_ime'] == korisnik['korisnicko_ime'] and lz['lozinka'] == korisnik['lozinka']:
            return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."

    return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija je neuspješna."


async def main():
    start = time.time()

    korisnici = [
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com', 'lozinka': 's324SDFfdsj234'},
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'pogresna_lozinka'}
    ]

    task = [asyncio.create_task(autorizacija(korisnik)) for korisnik in korisnici]
    rezultati = await asyncio.gather(*task)
    for rezultat in rezultati:
        print(rezultat)
    end = time.time()
    print(end - start)


asyncio.run(main())
