# Using a ThreadPoolExecutor
import concurrent.futures
from time import sleep, ctime

def thread_function(name):
  """
  This function blocks for 2 seconds and then prints a message.

  Args:
      name (str): The name of the thread.
  """
  sleep(2)
  print(f"{ctime()} {name}: starting")

if __name__ == "__main__":
  # Create a thread pool with 3 worker threads
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Submit three tasks to the executor
    futures = executor.map(thread_function, range(3))
    # Wait for all tasks to finish
    for future in futures:
      future.result()
  print(f"{ctime()} Main: All threads are finished")
