import multiprocessing
from time import sleep

# main_list = []

def update_main_list(shared_list, proc_num, n):
    for i in range(n):
        shared_list.append(f"{proc_num}_{i}")
    print(shared_list)


if __name__ == "__main__":
    n = 10
    count = 4
    procs = []
    manager = multiprocessing.Manager()
    shared_list = manager.list()

    for i in range(count):
        procs.append(multiprocessing.Process(target=update_main_list, args=[shared_list, i + 1, n]))

    for proc in procs:

        proc.start()

    for proc in procs:
        proc.join()

    print("Main list")
    main_list = list(shared_list)
    print(main_list)