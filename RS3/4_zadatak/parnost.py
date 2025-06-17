import asyncio, random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran"
    return f"Broj {broj} je neparan"


async def main():
    random_numbers = random.sample(range(1,101), 10)

    zadatci = [asyncio.create_task(provjeri_parnost(number)) for number in random_numbers]

    rezultati = await asyncio.gather(*zadatci)

    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())