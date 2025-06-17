import aiohttp, asyncio

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    cat_fact = await response.json()
    return cat_fact

async def filter_cat_facts(cat_list):
    print("Filtriranje činjenica o mačkama: ")
    filter_cat = []
    for element in cat_list:
        if "cat" in element["fact"] or "cats" in element["fact"]:
            filter_cat.append(element)
    return  filter_cat

async def main():
    async with aiohttp.ClientSession() as session:
        create_cat_task = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
        list_fact_cat = await asyncio.gather(*create_cat_task)

        filter_cat = await filter_cat_facts(list_fact_cat)

    for fact in list_fact_cat:
        print(f"- {fact}")
    for fact in filter_cat:
        print(f"- {fact}")
asyncio.run(main())
