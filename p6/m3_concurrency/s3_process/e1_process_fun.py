"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

The class Process on a function
"""

import multiprocessing
import time


def worker():
    cur = multiprocessing.current_process()
    print(f"{cur.name} ({cur.pid}) started")
    time.sleep(1)
    print(f"{cur.name} ({cur.pid}) terminating")


if __name__ == "__main__":
    cur = multiprocessing.current_process()
    print(f"{cur.name} ({cur.pid}) started")
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()
    print(f"{cur.name} ({cur.pid}) terminating")
