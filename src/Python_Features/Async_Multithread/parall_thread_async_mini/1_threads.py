import threading


def print_number(start, finish):
    for i in range(start, finish):
        print(i)


if __name__ == "__main__":
    threads = []
    for i in range(1, 6):
        threads.append(threading.Thread(target=print_number, args=(i * 100, i * 100 + 10)))

    for thread in threads:
        thread.start()
    # thread = threading.Thread(target=print_number, args=(1, 10))
    # thread.start()
    # thread.join()
    # print_number(51, 60)