from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(food):
    # generate a random value between 0 and 1
    cook_time = 1 + random()
    # report the value
    print(f'microwave ({food}): cooking for {cook_time} seconds...')
    await asyncio.sleep(cook_time)
    print(f'microwave ({food}): Finished cooking')
    return food, cook_time

# main coroutine
async def main():
    # create many tasks
    tasks = [
        asyncio.create_task(task_coro('rice')),
        asyncio.create_task(task_coro('noodle')),
        asyncio.create_task(task_coro('curry'))
    ]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f'completed task: {len(done)}')
    
    # process the first completed task
    completed_task = done.pop()
    meal, cook_time = await completed_task
    print(f' - {meal} cooked for {cook_time:.9f} seconds')
    
    print(f'Uncompleted task: {len(pending)}')


# run the main coroutine
asyncio.run(main())
