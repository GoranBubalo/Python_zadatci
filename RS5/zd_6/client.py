import asyncio, aiohttp, time
from aiohttp import web

async def send_request(url,port):
    async with aiohttp.ClientSession() as session:   
        response = await session.get(f'http://{url}:{port}/pozdrav')
        return await response.json()

async def main():
     start = time.time()
     
     response = await asyncio.gather(send_request('localhost', 8081), send_request('localhost', 8082))
     print (response)
     
     
     # Sekvencijalan dio koda 
     """service_response = await send_request('localhost', 8081)
     print(f"Odgovor servisa je :  {service_response}")
     
     service_response = await send_request('localhost', 8082)
     print(f"Odgovor servisa je :  {service_response}")"""
     end = time.time()
     
     print(f"Vrijeme potrebno za izvršavanje je {end - start:.2f}")
asyncio.run(main())