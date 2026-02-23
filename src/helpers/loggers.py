import logging
from typing import Optional

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def get_logger(name: Optional[str] = "app") -> logging.Logger:
    """returns a logger instance with the specified name"""
    return logging.getLogger(name)
