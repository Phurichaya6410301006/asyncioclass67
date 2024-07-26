import asyncio
import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_paris = 30

#Again notice that I doclare the main() function as a async function.
async def main(x):
    board_start_time = time.perf_counter()
    for i in range(move_paris):
        #print(f"BOARD-{x} {i+1} Judit thinkings of making a move.)
        #Don't use time.sleep in a async function. I'm using it becauuse in reality you aren't thinking about making.
        #move on 24 boards at the same time and so I need to black the event loop.
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move")
        await asyncio.sleep(opponent_compute_time)
    print(f"BOARD-{x+1} - >>>>>>>>>>>> Finished move in {round(time.perf_counter()- board_start_time)} ")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    #Again same structure as in async_io.py
    tasks = []
    for i in range(opponents):
        tasks +=[main(i)]
    await asyncio.gather(*tasks)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} seconds.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")