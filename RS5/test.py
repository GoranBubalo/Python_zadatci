from aiohttp import web
import asyncio, aiohttp
from aiohttp.web import AppRunner

async def get_users(request):
    user_id = request.match_info.get('id')
    
    korisnici = [
    {"id": 1, "ime": "Ivo", "godine": 25},
    {"id": 2, "ime": "Ana", "godine": 22},
    {"id": 3, "ime": "Marko", "godine": 19},
    {"id": 4, "ime": "Maja", "godine": 21},
    {"id": 5, "ime": "Iva", "godine": 40}
    ]
    
    if user_id is None:
        return web.json_response(korisnici, status=200)
    
    
    for korisnik in korisnici:
        if korisnik['id'] == int(user_id):
            return web.json_response(korisnik,status=200)
    
    return web.json_response({"Error" : "Korisnik s trenim id-om ne postoji"}, status=404)
    
    
app = web.Application()

app.add_routes([
    web.get('/korisnici', get_users),
    web.get('/korisnici/{id}',get_users)
])


async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Poslužitelj sluša na 8080")

async def main():
    await start_server()
    async with aiohttp.ClientSession() as session:
      rezultat = await session.get('http://localhost:8080/korisnici/6')
      rezultat_txt = await rezultat.text()
      print(rezultat_txt)
      
      rezultat_dict = await rezultat.json()
      print(rezultat_dict)

asyncio.run(main())


