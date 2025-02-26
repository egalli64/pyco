"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

The class Thread - subclass with run()
"""

import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(self.name, "has started")
        time.sleep(1)
        print(self.name, "terminating")


if __name__ == "__main__":
    print(threading.current_thread().name, "has started")
    thread = Worker(name="worker")
    thread.start()
    thread.join()
    print(threading.current_thread().name, "terminating")
