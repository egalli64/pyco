"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 5 - Log and Test

The logging module
"""

import logging
from e2_other import other

# logger for the current script
logger = logging.getLogger("e1_logging")

# log messages, by default to stderr
logger.debug("A debug message")
logger.info("An info message")
# by default, only message with severity warning or more are logged
logger.warning("A warning message")
logger.error("An error message")
logger.critical("A critical message")

print("Hello")

# change the log configuration: set log level, file sink, message format
logging.basicConfig(
    level="DEBUG",
    filename="p5_m7_s3.log",
    format="%(asctime)s %(levelname)-8s %(name)s:%(lineno)d %(message)s",
)

# log messages
logger.debug("A debug message")
logger.info("An info message")
logger.warning("A warning message")
logger.error("An error message")
logger.critical("A critical message")

# calling a function in another module with its own logger
other(42)
