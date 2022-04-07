from threading import Thread


def f(name):
    print("Hello", name)


if __name__ == "__main__":
    th = Thread(target=f, args=("Bob", ))
    th.start()
    th.join()
