import logging
import threading
import time


def thread_func(name):
    logging.info(f"Thread {name} starting")
    time.sleep(2)
    logging.info(f"thread {name} finishing")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H-%M-%S")
    logging.info("Main: before creating thread")
    x = threading.Thread(target=thread_func, args=(1,))
    logging.info("Main: before running thread")
    x.start()
    logging.info("Main: wait for the thread finish")
    logging.info("Main: all done")