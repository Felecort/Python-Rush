import multiprocessing
from time import sleep
from random import randint


def sleep_random_time(process_name):
    while True:
        sleep_for = randint(0, 100) / 50
        print(f"{process_name} will sleep for {sleep_for:.1f}s...")
        sleep(sleep_for)
        print(f"{process_name} awake!")


if __name__ == "__main__":
    processes = []
    p_count = 4
    for p in range(p_count):
        name = f"{p}_process"
        processes.append(multiprocessing.Process(target=sleep_random_time, args=[name]))
    for process in processes:
        process.start()
        # process.join()
