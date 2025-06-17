from aiohttp import web
import asyncio

async def get_response(request):
    await asyncio.sleep(4)
    return web.json_response({"message" : "Pozdrav nakon 4 sekunde"})

app = web.Application()

app.add_routes([
    web.get('/pozdrav', get_response)
])

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8082)