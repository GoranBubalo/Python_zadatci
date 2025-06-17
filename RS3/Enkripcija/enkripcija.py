import asyncio

async def secure_data(podatak):
    await asyncio.sleep(3)

    # Vraćamo enkriptirani rječnik
    return {
        'prezime': podatak['prezime'],
        'broj_kartice': hash(str(podatak['broj_kartice'])),
        'CVV': hash(str(podatak['CCV']))
    }

async def main():
    # Definiramo listu osjetljivih podataka
    podatci = [
        {'prezime': 'Bubalo', 'broj_kartice': 809912331511, 'CCV': 556},
        {'prezime': 'Drušković', 'broj_kartice': 999912332341, 'CCV': 445},
        {'prezime': 'Bilić', 'broj_kartice': 809111338881, 'CCV': 117},
    ]

    # Kreiramo zadatke za svaki rječnik
    zadaci = [asyncio.create_task(secure_data(podatak)) for podatak in podatci]

    # Pokrećemo sve zadatke i prikupljamo rezultate
    rezultati = await asyncio.gather(*zadaci)

    # Ispisujemo rezultate
    for rez in rezultati:
        print(rez)

    # Pokrećemo glavni program


asyncio.run(main())