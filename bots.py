import threading
import time
import json

# Load inventory from file
with open('inventory.dat') as json_file:
    inventory = json.load(json_file)

def bot_fetcher(items, cart, lock):
    for item in items:
        time.sleep(inventory[item][1])
        lock.acquire()
        cart.append([item, inventory[item][0]]) 
        lock.release()

def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    fetcher_lists = [items[i::3] for i in range(3)]
    threads = []

    for fetcher_list in fetcher_lists:
        thread = threading.Thread(target=bot_fetcher, args=(fetcher_list, cart, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cart
