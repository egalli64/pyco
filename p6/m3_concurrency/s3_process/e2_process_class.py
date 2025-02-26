"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

The class Process - subclass with run()
"""

import multiprocessing
import time


class Worker(multiprocessing.Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f"{self.name} ({self.pid}) started")
        time.sleep(1)
        print(f"{self.name} ({self.pid}) terminating")


if __name__ == "__main__":
    cur = multiprocessing.current_process()
    print(f"{cur.name} ({cur.pid}) started")
    process = Worker(name="worker")
    process.start()
    process.join()
    print(f"{cur.name} ({cur.pid}) terminating")
