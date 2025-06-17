from aiohttp import web
import asyncio

async def get_function(request):
    # Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina
    data = {'naziv' : 'Kola', 'Cijena' : 2.30, 'Količina' : '20'}
    
    # Serijalizacija
    return web.json_response(data)

async def post_function(request):
    data = await request.json()
    return  web.json_response(data)

app = web.Application()


app.router.add_routes([
    web.get('/proizvodi', get_function),
    web.post('/proizvodi', post_function)
])

web.run_app(app, host='localhost', port=8081)

