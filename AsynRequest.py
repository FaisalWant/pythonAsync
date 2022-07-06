from datetime import datetime 
from pprint import pprint 
import asyncio 


import aiohttp 
import click 

urls=[

"https:/httpbin.org/get?text=python",
"https:/httpbin.org/get?text=is",
"https:/httpbin.org/get?text=fun",
"https:/httpbin.org/get?text=and",
"https:/httpbin.org/get?text=useful",
"https:/httpbin.org/get?text=you",
"https:/httpbin.org/get?text=can",
"https:/httpbin.org/get?text=almost",
"https:/httpbin.org/get?text=do",
"https:/httpbin.org/get?text=anything", 

]

async def fetch_args(session, url): 
    async with session.get(url) as response: 
        data= await response.json() 
        return data["args"] 
    

async def main(): 
    async with aiohttp.ClientSession() as session: 
        # create a collection of coroutines (can be done with comprehension) 
        fetch_coroutines=[] 
        for url in urls: 
            fetch_coroutines.append(fetch_args(session, url)) 
        
        # wake up coroutine with gather 
        data = await asyncio.gather(*fetch_coroutines) 
        pprint(data) 




start= datetime.now() 
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white") 