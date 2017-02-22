import logging

logging.basicConfig(filename='decorated.log', level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def log_order_event(func):
    def wrapper(*args, **kwargs):
        logging.info("Ordering: %s", func.__name__)
        order = func(*args, **kwargs)
        logging.debug("Order result: %s", order)
        return order
    return wrapper

@log_order_event
def order_pizza(*toppings):
    # let's get some pizza!
    print("Pizza ordered:")
    for topping in toppings:
        print(topping)
    return len(toppings)

order_pizza("Pineapple", "Ham")