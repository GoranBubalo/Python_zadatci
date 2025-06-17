from aiohttp import web
import asyncio, aiohttp

async def get_response(request):
    await asyncio.sleep(3)
    return web.json_response({"message" : "Pozdrav nakon 3 sekunde"})

app = web.Application()

app.add_routes([
    web.get('/pozdrav', get_response)
])

if __name__ == "__main__":
    web.run_app(app,host='localhost', port=8081)