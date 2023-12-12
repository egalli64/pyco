"""
Python Course

https://github.com/egalli64/pyco

Module 11 - Log and Test

The logging module
"""
import logging
from s3_other import other

# logger for the current file
logger = logging.getLogger("s3_logging")

# log messages
logger.debug("A debug message")
logger.info("An info message")
logger.warning("A warning message")
logger.error("An error message")
logger.critical("A critical message")

print("Hello")

# change the log configuration
logging.basicConfig(
    level="DEBUG",
    filename="s3_my_app.log",
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
