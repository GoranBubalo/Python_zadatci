from aiohttp import web 
import asyncio

async def post_data(request):
    await asyncio.sleep(2)
    data = await request.json()
    sum_data = data.get('data_sum')
    mul_data = data.get('data_mul') 
    
    if  sum_data  is None and sum_data == 0:
        return web.json_response({"Error" : "Can't devide with 0"},status=400)
    
    kolicnik = mul_data / sum_data
    return web.json_response({"kolicnik" : kolicnik}, status=200)
    
    
    

app = web.Application()


app.add_routes([
    web.post('/kolicnik', post_data)
])

if __name__ == '__main__':
    web.run_app(app,host='localhost', port=8085)