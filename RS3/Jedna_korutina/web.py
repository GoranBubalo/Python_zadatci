import asyncio
import time


async def dohvacanje_podatka():
    list_brojeva = [number for number in range(1, 11)]
    await asyncio.sleep(3)
    print("Podatci dohvaćeni")
    return  list_brojeva

async def main():
    start = time.time()
    await dohvacanje_podatka()
    end = time.time()
    print(f"{end - start}")


asyncio.run(main())