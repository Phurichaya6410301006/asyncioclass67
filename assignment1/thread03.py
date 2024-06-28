# Extending the Thread class
from time import sleep, ctime

from threading import Thread

# Custom thread class
class CustomThread(Thread):
    def __init__(self):
        super().__init__()  # Call the base class constructor

    # Override the run function
    def run(self):
        sleep(1)  # Block for a moment
        print(f'{ctime()} This is coming from another thread')

# Create the thread
thread = CustomThread()

# Start the thread
thread.start()

# Wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thread.join()
