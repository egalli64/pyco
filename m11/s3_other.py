"""
Python Course

https://github.com/egalli64/pyco

Module 11 - Log and Test

The logging module
"""
import logging

# logger for the current file
logger = logging.getLogger("s3_other")


def other(value):
    logger.debug(f"Enter other({value})")


if __name__ == "__main__":
    print("This module is meant to be imported by the logging main script")