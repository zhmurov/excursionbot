"""Logging configuration for the Location Facts Bot."""
import logging
import sys
from typing import NoReturn

from config import LOG_LEVEL

def setup_logging() -> NoReturn:
    """Configure logging for the application."""
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)

    # Create console handler with formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(LOG_LEVEL)
    
    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)

    # Add console handler to the logger
    logger.addHandler(console_handler)

    # Suppress unnecessary logs from libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("telegram").setLevel(logging.WARNING) 