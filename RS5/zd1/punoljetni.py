from aiohttp import web
import asyncio

korisnici = [
 {'ime': 'Ivo', 'godine': 25},
 {'ime': 'Ana', 'godine': 17},
 {'ime': 'Marko', 'godine': 19},
 {'ime': 'Maja', 'godine': 16},
 {'ime': 'Iva', 'godine': 22}
]

async def get_function(request):
    mature_list = list(filter(lambda x: x['godine'] > 18, korisnici))
    #mature_list_comprehension = [i for i in korisnici if i['godine'] > 18]
    return web.json_response(mature_list)

app = web.Application()


#app.router.add_get('punoljetni',get_function)

app.add_routes([
    web.get('/punoljetni',get_function)
])

web.run_app(app, host='localhost', port=8082)