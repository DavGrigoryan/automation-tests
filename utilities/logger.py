import logging
import os
from datetime import datetime

# Create a custom logger
logger = logging.getLogger("Automation")

# Set the default logging level (could be changed to DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Log file handler
log_directory = "reports/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Use the current date for the log filename in the desired format
log_filename = f"{log_directory}/log-{datetime.now().strftime('%Y-%m-%d')}.log"
file_handler = logging.FileHandler(log_filename, mode='a')  # 'a' mode to append to the file if it exists
file_handler.setLevel(logging.DEBUG)

# Create formatters and add them to handlers
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger if they haven't been added already
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
