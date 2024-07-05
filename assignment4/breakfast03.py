# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():  # Task 1
    print("coffee: prepare ingredients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5)  # Pause, another tasks can be run
    print("coffee: ready!")

async def fry_eggs():  # Task 2
    print("eggs: prepare ingredients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)  # Pause, another tasks can be run
    print("eggs: ready!")

async def main():
    start = time()
    # Run tasks concurrently
    coffee_task = asyncio.create_task(make_coffee())
    eggs_task = asyncio.create_task(fry_eggs())
    
    await coffee_task
    await eggs_task
    print(f"Breakfast is ready in {time()-start} min")

asyncio.run(main())  # Run top-level function concurrently