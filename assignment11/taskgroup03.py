import time
import asyncio
from asyncio import Queue

# Define Product and Customer classes
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

# Consumer method to process customers in queue
async def checkout_customer(queue: Queue, cashier_number: int, cashier_stats: dict, checkout_times: list[float]):
    customers_served = 0  # Track number of customers served by each cashier
    cashier_start_time = time.perf_counter()
    
    while not queue.empty():
        customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"Cashier_{cashier_number} will checkout Customer_{customer.customer_id}")
        
        # Use the specific checkout time for this cashier
        for product in customer.products:
            await asyncio.sleep(checkout_times[cashier_number])  # Simulate checkout time
        
        print(f"Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} in {round(time.perf_counter() - customer_start_time, 2)} seconds")
        customers_served += 1
        queue.task_done()
    
    total_time = round(time.perf_counter() - cashier_start_time, 2)
    cashier_stats[cashier_number] = (customers_served, total_time)  # Save stats for each cashier

# Generate a customer with predefined checkout time for products
def generate_customer(customer_id: int) -> Customer:
    # Since the checkout time is now defined per cashier, we can set a dummy time here
    products = [Product('product', 0)]  # Dummy time
    return Customer(customer_id, products)

# Producer method to generate customers and put them in the queue
async def customer_generation(queue: Queue, customers: int):
    for customer_id in range(customers):
        customer = generate_customer(customer_id)
        print(f"Putting Customer_{customer_id} in line...")
        await queue.put(customer)
    return customers

# Main function to run the specific test case
async def main():
    # Specific test case: Queue = 5, Customers = 10, Cashiers = 5, with specific checkout times
    
    customers = 4
    queue_size = 2
    cashiers = 2
    checkout_times = [2.0, 2.4, 0.4, 3.2, 3.6]  # Specific checkout times for each cashier

    customer_queue = Queue(queue_size)
    cashier_stats = {}  # Dictionary to store stats for each cashier

    start_time = time.perf_counter()

    # Create the producer task
    customer_producer = asyncio.create_task(customer_generation(customer_queue, customers))

    # Create the consumer tasks for cashiers
    cashier_tasks = [checkout_customer(customer_queue, i, cashier_stats, checkout_times) for i in range(cashiers)]

    # Run all tasks concurrently
    await asyncio.gather(customer_producer, *cashier_tasks)

    # Sort and print statistics for each cashier by cashier number
    sorted_stats = sorted(cashier_stats.items())  # Sort by cashier number
    for cashier_number, (customers_served, total_time) in sorted_stats:
        print(f"The Cashier_{cashier_number} took {customers_served} customers total {total_time:.2f} seconds")

    # Print total time taken for all customers
    print(f"Total Time for {customers} customers with {cashiers} cashiers: {round(time.perf_counter() - start_time, 2)} seconds")

if __name__ == "__main__":
    asyncio.run(main())