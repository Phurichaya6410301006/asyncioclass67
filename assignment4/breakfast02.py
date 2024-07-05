# Concurrently breakfast
import asyncio
from time import sleep, time


async def make_coffee(): # 1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5) # 2: pause, another tasks can be run
    print("coffee: ready")
    
async def fry_eggs(): #1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("eggs: ready")
    
async def main(): #1
    start = time()
    await make_coffee() # run task with await
    await fry_eggs()
    print(f"breakfast is ready in {time()-start} min")
    
    
asyncio.run(main()) # run top-level function concurrently