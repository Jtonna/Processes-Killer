import logging
import os

class Logger:
    def __init__(self):
        logging.basicConfig(format="[%(levelname)s] %(message)s; %(asctime)s", filename="process_killer.log", filemode="w", level=logging.DEBUG)

    def info(self, value):
        logging.info(value)

    def debug(self, value):
        logging.debug(value)

    def warning(self, value):
        logging.warning(value)

    def error(self, value):
        logging.error(value)
    
    def critical(self, value):
        logging.critical(value)

log = Logger()