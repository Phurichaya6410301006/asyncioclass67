# Working With Many Threads
# Working with multiple threads

from time import sleep, ctime

from threading import Thread

def thread_function(name, sleep_time):
    """
    This function blocks for a specified time and then prints a message.

    Args:
        name (str): The name of the thread.
        sleep_time (float): The amount of time to sleep in seconds.
    """
    sleep(sleep_time)
    print(f"{ctime()} {name}: Thread function executed")

# Create and start three threads
threads = list()
for index in range(3):
    thread = Thread(target=thread_function, args=(f"Thread {index}", 1.5))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"{ctime()} Main: All threads are finished")
