import time
import asyncio
from asyncio import Queue
from random import randrange

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
async def checkout_customer(queue: Queue, cashier_number: int):
    dict_cashier = {"customer": 0, "total": 0}
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number } "
              f"will checkout Customer_{customer.customer_id}")
        for product in customer.products:
            if cashier_number == 2:
                product.checkout_time = 0.1
            else:
                product.checkout_time = product.checkout_time + (0.1*cashier_number)

            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}"
                  f" Product_{product.product_name}"
                  f" in {round(product.checkout_time, ndigits=2)} secs")
            await asyncio.sleep(product.checkout_time)
        print(f"The Cashier_{cashier_number} "
              f"finished checkout Customer_{customer.customer_id}"
              f" in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")
        
        dict_cashier["customer"] += 1
        dict_cashier["total"] += round(time.perf_counter() - customer_start_time, ndigits=2)
        queue.task_done()

    return cashier_number, dict_cashier

# Generate a customer with predefined checkout time for products
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# Producer method to generate customers and put them in the queue
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count+customers)]
        for customer in customers:
            print(f"Waiting to put Customer_{customer.customer_id} in line.... ")
            await queue.put(customer)
            print(f"Customer_{customer.customer_id} put in line...")
        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count

# Main function
async def main():
    CUSTOMER = 10
    QUEUE = 3
    CASHIER = 5
    customer_queue = Queue(QUEUE)
    customers_start_time = time.perf_counter()

    async with asyncio.TaskGroup() as group:
        customer_producer = group.create_task(customer_generation(customer_queue, CUSTOMER))
        cashiers = [group.create_task(checkout_customer(customer_queue, i)) for i in range(CASHIER)]
        
    results = [cashier.result() for cashier in cashiers]

    print("----------------")
    for result in results:
        print(f"The Cashier_{result[0]} "
              f"take {result[1]['customer']} "
              f"customers total {result[1]['total']} secs")
        
    print(f"The supermarket process finished "
          f"{customer_producer.result()} customers "
          f"in {round(time.perf_counter() - customers_start_time, ndigits=2)} secs")

if __name__ == "__main__":
    asyncio.run(main())
