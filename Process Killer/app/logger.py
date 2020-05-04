import logging
import logging.config
import tempfile

class Logger:
    def __init__(self):
        x = tempfile.gettempdir()
        y = x+"\process_killer.log"
        print(y)
        logging.basicConfig(format="[ %(asctime)s %(levelname)s]: %(message)s", filename=y, filemode="w", level=logging.DEBUG)

    def info(self, value):
        logging.info(value)

    def debug(self, value):
        logging.debug(value)

    def warn(self, value):
        logging.warning(value)

    def error(self, value):
        logging.error(value)
    
    def critical(self, value):
        logging.critical(value)

log = Logger()