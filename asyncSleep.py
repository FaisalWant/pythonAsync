
 #blocking code
import time 
from datetime import datetime 
import click 
import asyncio



#-------------------------------------------------------   blocking code 

# def sleep_and_print(seconds): 
#     print(f"starting{seconds} sleep :)")
#     time.sleep(seconds) 
#     print(f"finished {seconds} sleep") 
#     return seconds 



# start = datetime.now()
# print([sleep_and_print(3), sleep_and_print(6)])
# click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")


#--------------------------------------------------------- Non blocking code

async def sleep_and_print(seconds): 
    print(f"starting async{ seconds} sleep") 
    await asyncio.sleep(seconds) 
    print(f"finished async{seconds} sleep") 
    return seconds 


async def main(): 

    results= await asyncio.gather(sleep_and_print(3), sleep_and_print(6)) 

    # building list 
    coroutines_list=[]

    for i in range(1,11): 
        coroutines_list.append(sleep_and_print(i)) 

    result= await asyncio.gather(*coroutines_list)   # gather takes arguments, not list 
    print(results) 



start= datetime.now()
asyncio.run(main())
