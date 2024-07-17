import logging
import os
from datetime import datetime


class DelayedFileHandler(logging.Handler):
    def __init__(self, log_directory):
        super().__init__()
        self.log_directory = log_directory
        self.file_handler = None

    def create_file_handler(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        log_filename = f"{self.log_directory}/log-{datetime.now().strftime('%Y-%m-%d')}.log"
        self.file_handler = logging.FileHandler(log_filename, mode='a')
        self.file_handler.setLevel(logging.DEBUG)

        file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(file_format)

    def emit(self, record):
        if self.file_handler is None:
            self.create_file_handler()
        self.file_handler.emit(record)


def configure_logger():
    internal_logger = logging.getLogger("Automation")
    internal_logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    if not internal_logger.hasHandlers():
        internal_logger.addHandler(console_handler)
        internal_logger.addHandler(DelayedFileHandler("reports/logs"))

    return internal_logger


logger = configure_logger()
