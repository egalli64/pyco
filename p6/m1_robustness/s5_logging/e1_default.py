"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

The logging module - default usage
"""

import logging

# logger for the current script
logger = logging.getLogger("e1_logging")

# log messages, by default to stderr
logger.debug("log: a debug message - by default disabled")
logger.info("log: an info message - by default disabled")
# by default, only message with severity warning or more are logged
logger.warning("log: a warning message")
logger.error("log: an error message")
logger.critical("log: a critical message")

print("Hello")
