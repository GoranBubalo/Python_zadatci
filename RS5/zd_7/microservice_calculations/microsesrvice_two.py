from aiohttp import web
import asyncio

async def calculation_multiplier(request):
    await asyncio.sleep(2)
    data = await request.json()
    
    if not data:
        return web.json_response({"Error" : "No data hase been found"}, status=404)
    
    get_data = data.get('podatci')
    starting_val = 1
    ##TODO :Make a list comprehension version 
    #list_comprehension = [starting_val * cal for cal in get_data]
    for val in get_data:
        starting_val = starting_val * val
    return web.json_response({"totla multiply" : starting_val},status=200)
    
    

app = web.Application()

app.add_routes([
    web.post('/umnozak', calculation_multiplier)
])

if __name__ == '__main__':
    web.run_app(app,host='localhost', port=8084)