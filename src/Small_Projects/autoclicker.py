import threading
import keyboard
import pyautogui
from time import sleep
from threading import Thread


class AutoClicker:

    def __init__(self):
        self.click_flag = -1
        self.clicker_run = True

    lock = threading.Lock()

    def wait_key(self):
        keyboard.hook(self.change_flag)
        keyboard.wait('e')

    def click_mouse(self):
        while self.clicker_run:
            sleep(0.1)
            if self.click_flag == 1:
                pyautogui.click()

    def change_flag(self, e):
        if e.name == 'x' and e.event_type == 'up':
            self.click_flag *= -1
        elif e.name == 'e' and e.event_type == 'up':
            self.clicker_run = False

    def run(self):
        thread1 = Thread(target=self.wait_key, args=())
        thread2 = Thread(target=self.click_mouse, args=())

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()


if __name__ == "__main__":
    clicker = AutoClicker()
    clicker.run()
