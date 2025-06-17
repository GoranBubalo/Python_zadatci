import aiohttp, asyncio, time

async def dohvati_sum_podataka(session,data_json):
    response = await session.post('http://localhost:8083/zbroj',json=data_json)
    return await response.json()

async def dohvati_mul_podataka(session,data_json):
    response = await session.post('http://localhost:8084/umnozak',json=data_json)
    return await response.json()


async def main():
    start = time.time()
    
   
    data = [i for i in range (1,11)]
    data_json = {'podatci' : data}
    async with aiohttp.ClientSession() as session:
        
        # Konkurentno
        sum_data, mul_data = await asyncio.gather(dohvati_sum_podataka(session,data_json),dohvati_mul_podataka(session,data_json))
        
        # ekstrakcija podataka
        sum_data_ecxtracting = sum_data.get('sum')
        mul_data_ecxtracting = mul_data.get('totla multiply')
        
        data_json = {
            "data_sum" : sum_data_ecxtracting, 
            "data_mul" :  mul_data_ecxtracting
            }
        resoult_kol = await session.post('http://localhost:8085/kolicnik',json=data_json)
        resoult_kol_data = await resoult_kol.json()
        print(resoult_kol_data)
        end = time.time()
        
        print(f"Time to complete program is : {end-start:.2f}")

asyncio.run(main())