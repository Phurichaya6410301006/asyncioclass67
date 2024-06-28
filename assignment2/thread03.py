# Thread version of cooking 1 kitchen 1 chefs 1 dishes
import os
from time import time, sleep, ctime
import threading

def cooking(index):
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID {os.getpid()}')
    cooking_time = time()
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID')
    sleep(2)
    duration = time() - cooking_time
    basket.use_eggs(index)
    print(f'{ctime()} Kitchen - {index} : Cooked done in {duration:0.2f} seconds!')

class Basket:
    def __init__(self):
        self.eggs = 50
        self._lock = threading.Lock()
    def use_eggs(self, index):
        with self._lock:
            print(f'{ctime()} Kitchen - {index} : Chef - {index} has lock with eggs remaining {self.eggs}')
            self.eggs -= 1
            print(f'{ctime()} Kitchen - {index} : Chef - {index} has release lock with eggs remaining {self.eggs}')

if __name__ == "__main__":
    #Begin of main thread
    print(f'{ctime()} Main          : Start Cooking...')

    start_time = time()

    basket = Basket()

    print(f'{ctime()} Main          : ID of main process: {os.getpid()}')

    #multithread cooking
    chefs = list()
    for index in range(2):
        c = threading.Thread(target=cooking, args=(index,))
        chefs.append(c)
        c.start()

    for index, c in enumerate(chefs):
        c.join()

    print(f'{ctime()} Main          : Basket egg remaining {basket.eggs}')
    duration = time() - start_time
    print(f'{ctime()} Main          : Finished Cooking duration in {duration:0.2f} seconds')