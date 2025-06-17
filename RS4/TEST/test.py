import aiohttp, asyncio, time

async def get_cat_fact(session,i):
    print("Šaljemo zahtjev za mačji fact")
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    print(f"{i + 1}: {fact_dict['fact']}")

async def main():
    stat = time.time()
    async with aiohttp.ClientSession() as session:
        get_cat_task = [asyncio.create_task(get_cat_fact(session,i)) for i in range(5)]
        actual_cat_fact = await asyncio.gather(*get_cat_task)

    end = time.time()
    print(end - stat)

asyncio.run(main())