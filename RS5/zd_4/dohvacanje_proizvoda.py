from aiohttp import web
import aiohttp, asyncio
from aiohttp.web import AppRunner

proizvodi = [
 {"id": 1, "naziv": "Laptop", "cijena": 5000},
 {"id": 2, "naziv": "Miš", "cijena": 100},
 {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
 {"id": 4, "naziv": "Monitor", "cijena": 1000},
 {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

order = []

app = web.Application()


async def get_product(request):
    product_id = request.match_info.get('id')
    
    if not product_id:
        return web.json_response(proizvodi, status=200)
    
    for product in proizvodi:
        if product['id'] == int(product_id):
            return web.json_response(product, status=200)
    
    return web.json_response({"Error" : "Product does not exist!!"}, status=404)


async def get_order(request):
    data = await request.json()
    order_id = data.get('proizvodi_id')
    kolicina = data.get('kolicina')
    
    for product in proizvodi:
        if product['id'] == int(order_id):
            dict_list = {"product_id" : order_id, "kolicina" : kolicina}
            order.append(dict_list)
            return web.json_response(order, status=201)
    return web.json_response({"Error" : "order_id does not match product_id"}, status=404)


app.add_routes([
    web.get('/proizvodi', get_product),
    web.get('/proizvodi/{id}',get_product),
    web.post('/narudzbe', get_order)
])


async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8081")

async def main():
    await start_server()
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://localhost:8081/proizvodi/3')
        response_json = await response.json()
        print(response_json)
        
        
        post_url = 'http://localhost:8081/narudzbe'
        post_data = {"proizvodi_id" : 3, "kolicina" : 2}
        post_resposne = await session.post(post_url, json = post_data)
        post_resposne_json = await post_resposne.json()
        print(post_resposne_json)
        

asyncio.run(main())