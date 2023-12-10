import logging
import sys


class CustomFormatter(logging.Formatter):
    """
    INFO - Кислотно-зеленый цвет: \033[92m
    DEBUG - Розовый цвет: \033[95m
    CRITICAL и ERROR - Красный цвет: \033[91m
    WARNING - Темно-желтый цвет: \033[93m
    """

    def __init__(self, fmt, datefmt=None):
        super().__init__(fmt, datefmt)
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: "\033[95m" + self.fmt + "\033[0m",
            logging.INFO: "\033[92m" + self.fmt + "\033[0m",
            logging.WARNING: "\033[93m" + self.fmt + "\033[0m",
            logging.ERROR: "\033[91m" + self.fmt + "\033[0m",
            logging.CRITICAL: "\033[91m" + self.fmt + "\033[0m"
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt.strip())
        return formatter.format(record)


LEVEL = logging.DEBUG
FILE_LOGS = 'log_info.log'

colored_formatter = CustomFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
plain_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(LEVEL)

file_handler = logging.FileHandler(FILE_LOGS)
file_handler.setLevel(LEVEL)
file_handler.setFormatter(plain_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(LEVEL)
stream_handler.setFormatter(colored_formatter)

aiogram_logger = logging.getLogger('aiogram')
aiogram_logger.setLevel(LEVEL)

aiogram_file_handler = logging.FileHandler(FILE_LOGS)
aiogram_file_handler.setLevel(LEVEL)
aiogram_file_handler.setFormatter(plain_formatter)

aiogram_stream_handler = logging.StreamHandler(sys.stdout)
aiogram_stream_handler.setLevel(LEVEL)
aiogram_stream_handler.setFormatter(colored_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
aiogram_logger.addHandler(aiogram_file_handler)
aiogram_logger.addHandler(aiogram_stream_handler)