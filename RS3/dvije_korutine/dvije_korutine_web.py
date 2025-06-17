import asyncio
import time


async def lista_dictionary():
    korisnici = [
        {'ime': 'Ivan', 'Prezime': 'Ivić', 'dob': 20},
        {'ime': 'Marko', 'Prezime': 'Markoć', 'dob': 22},
        {'ime': 'Stipe', 'Prezime': 'Stipić', 'dob': 19},
        {'ime': 'Jure', 'Prezime': 'Jurić', 'dob': 21},
    ]
    await asyncio.sleep(3)
    return korisnici


async def druga_lista_dictionary():
    proizvodi = [
        {'Naziv': 'Milka', 'cijena': 2, 'dostupna_kolicina': 34},
        {'Naziv': 'Coca-cola', 'cijena': 3, 'dostupna_kolicina': 15},
        {'Naziv': 'Kikiriki', 'cijena': 1, 'dostupna_kolicina': 8},
        {'Naziv': 'Mliko', 'cijena': 2, 'dostupna_kolicina': 12},
    ]
    await asyncio.sleep(5)
    return proizvodi


async def main():
    start = time.time()

    # rezultat1, rezultat2 = await asyncio.gather(lista_dictionary(), druga_lista_dictionary())

    rezultat1 = asyncio.create_task(lista_dictionary())
    rezultat2 = asyncio.create_task(druga_lista_dictionary())

    await rezultat1
    await rezultat2

    print(rezultat1)
    print(rezultat2)
    end = time.time()
    print(end - start)


asyncio.run(main())
