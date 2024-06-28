# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# share resources

# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctime, time

class Basket:
    def __init__(self):
        self.eggs = 50

    def use_egg(self, index):
        print(f'{ctime()} Kitchen - {index} : Chef - {index} has lock with eggs remaining {self.eggs}')
        self.eggs -= 1
        print(f'{ctime()} Kitchen - {index} : Chef - {index} release lock with eggs remaining {self.eggs}')

def kitchen(index, share_eggs):
    cooking_time = time()
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen - {index} : Cooked done in {duration:0.2f} seconds')

def cooking(index, basket):
    cooking(index)
    basket.use_egg(index)
    sleep(2)

if __name__ == "__main__":
    #Begin of main thread
    print(f'{ctime()} Main          : Start Cooking...PID {os.getpid()}')
    start_time = time()

    basket = Basket()

    # Multi kitchens with each chef
    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        kitchens.append(p)
        #starting process
        p.start()

    for index, p in enumerate(kitchens):
        #wait until process are finished
        p.join()

    print(f'{ctime()} Main          : Basket egg remaining {basket.eggs}')
    duration = time() - start_time
    print(f'{ctime()} Main          : Finished Cooking duration in {duration:0.2f} seconds')