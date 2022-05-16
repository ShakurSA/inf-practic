import time
import threading
import random


list_get_data = {}
list_write_to_console = {}
list_write_to_file = {}

data = 0
file = 0
console = 0


def get_data(task_id):
    print(f"processing get_data({task_id})")
    time.sleep(random.randint(1, 3))
    print(f"completed get_data({task_id})")


def write_to_file(task_id):
    print(f"processing write_to_file({task_id})")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_file({task_id})")


def write_to_console(task_id):
    print(f"processing write_to_console({task_id})")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_console({task_id})")

def obr_data(task_id):
    global data
    data += 1
    get_data(task_id)
    data -= 1


def obr_console(task_id):
    global console
    console += 1
    write_to_console(task_id)
    console -= 1


def obr_file(task_id):
    global file
    file += 1
    write_to_file(task_id)
    file -= 1


def MultiThreading(task_id):
    list_get_data[task_id] = threading.Thread(target=obr_data, args=(task_id,))
    while data > 10:
        time.sleep(1)
    list_get_data[task_id].start()
    list_get_data[task_id].join()
    list_write_to_file[task_id] = threading.Thread(target=obr_file, args=(task_id,))
    list_write_to_console[task_id] = threading.Thread(target=obr_console, args=(task_id,))

    while file > 5:
        time.sleep(1)
    list_write_to_file[task_id].start()
    while console > 1:
        time.sleep(1)
    list_write_to_console[task_id].start()


list = []
for task_id in range(1, 21):
    list[task_id] = threading.Thread(target=MultiThreading(task_id), args=(task_id,))
    list[task_id].start()

