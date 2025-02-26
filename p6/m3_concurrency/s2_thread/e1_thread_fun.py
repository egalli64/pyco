"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

The class Thread on a function
"""

import threading
import time


def worker():
    print(threading.current_thread().name, "has started")
    time.sleep(1)
    print(threading.current_thread().name, "terminating")


if __name__ == "__main__":
    print(threading.current_thread().name, "has started")
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()
    print(threading.current_thread().name, "terminating")
