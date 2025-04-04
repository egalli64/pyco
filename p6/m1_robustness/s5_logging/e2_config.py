"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

The logging module - with configuration
"""

import logging
from other import calculate_solution

# logger for the current script
logger = logging.getLogger("e1_logging")

# configure the log: set its level, file sink, message format
logging.basicConfig(
    level="DEBUG",
    filename="p6/m1_s5.log",
    format="%(asctime)s %(levelname)-8s %(name)s:%(lineno)d %(message)s",
)

# log messages
logger.debug("A debug message")
logger.info("An info message")
logger.warning("A warning message")
logger.error("An error message")
logger.critical("A critical message")

# calling a function in another module with its own logger
calculate_solution(6, 7)
