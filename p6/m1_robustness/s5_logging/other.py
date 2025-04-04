"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

The logging module - each module with its own logger, same configuration
"""

import logging

# logger for the current file
logger = logging.getLogger("other")


def calculate_solution(a, b):
    logger.debug(f"enter f({a}, {b})")
    print("The solution is", a * b)


if __name__ == "__main__":
    print("This module is meant to be imported by the logging main script")
