import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("Jarvis")

logger.setLevel(logging.INFO)

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File
    file_handler = logging.FileHandler(
        "logs/jarvis.log",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)