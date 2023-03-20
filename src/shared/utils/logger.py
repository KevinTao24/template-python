import logging
import sys
from logging.handlers import TimedRotatingFileHandler


def setup_logger(name=None, log_level=logging.INFO, log_file=None):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s"
    )

    if log_file:
        file_handler = TimedRotatingFileHandler(log_file, when="midnight")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
