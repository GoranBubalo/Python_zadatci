import aiohttp, asyncio


async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    dog_fact = await response.json()
    return dog_fact


async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    get_cat = await response.json()
    return get_cat


async def mix_facts(dog_facts, cat_facts):
    new_list = []
    for dog_list, cat in zip(dog_facts, cat_facts):
        for dog in dog_list:
            if len(dog) > len(cat):
                new_list.append(dog)
            elif len(dog) < len(cat):
                new_list.append(cat)
    return new_list



async def main():
    async with aiohttp.ClientSession() as session:
        dog_task = [asyncio.create_task(get_dog_fact(session)) for _ in range(6)]
        cat_task = [asyncio.create_task(get_cat_fact(session)) for _ in range(6)]
        dog_cat_facts = await asyncio.gather(*dog_task, *cat_task)
        dog_facts_all = dog_cat_facts[0:5]
        cat_facts_all = dog_cat_facts[6:11]



        dog_fact = [[dog['attributes']['body'] for dog in dog["data"]] for dog in dog_facts_all]
        cat_fact = [cat["fact"] for cat in cat_facts_all]

        facts = await mix_facts(dog_fact, cat_fact)
        for f in facts:
            print(f" - {f}")





asyncio.run(main())
