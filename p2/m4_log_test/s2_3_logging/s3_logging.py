"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Log and Test

The logging module
"""
import logging
from s3_other import other

# logger for the current script
logger = logging.getLogger("s3_logging")

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
