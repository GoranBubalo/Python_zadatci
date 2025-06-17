from aiohttp import web
import asyncio

async def post_sum(request):
    await asyncio.sleep(2)
    data = await request.json()
    
    if not data:
        return web.json_response({"Error" : {"Data is empty!!!, can't sum non-existend data"}},status=404)
    
    get_list_data = data.get('podatci')
    sum_data = sum(get_list_data)
    return web.json_response({"sum" : sum_data},status=200)

app = web.Application()

app.add_routes([
    web.post('/zbroj', post_sum)
])

if __name__ == '__main__':
    web.run_app(app,host='localhost', port=8083)