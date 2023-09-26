import multiprocessing
from time import sleep

# main_list = []

def update_main_list(queue, proc_num, n):
    main_list = queue.get()
    for i in range(n):
        main_list.append(f"{proc_num}_{i}")
    print(main_list)
    queue.put(main_list)


if __name__ == "__main__":
    n = 10
    count = 4
    procs = []
    queue = multiprocessing.Queue()
    queue.put([])

    for i in range(count):
        procs.append(multiprocessing.Process(target=update_main_list, args=[queue, i + 1, n]))

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    main_list = queue.get()
    print("Main list")
    print(main_list)