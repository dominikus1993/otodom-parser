import logging
from pythonjsonlogger import jsonlogger

def get_logger() -> logging.Logger:
    logger = logging.getLogger("otodom.parser")
    logger.setLevel(logging.DEBUG)
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logHandler.setLevel(logging.DEBUG)

    logger.addHandler(logHandler)
    return logger