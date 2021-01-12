"""Simple script for initializing things like logging and finding environment variables.
"""
import logging

from src.logger import logger, set_logger_file
try:
    from dotenv import load_dotenv
    #Export environment variables from .env
    load_dotenv()
except ModuleNotFoundError:
    # python-dotenv is not installed.
    pass

# This import needs to happen after dotenv loads the env variables.
from conf import config  # pylint: disable=wrong-import-position


set_logger_file(a_lg=logger, log_file_dir=config["name"])
conf_log_level = config["log_level"]

assert conf_log_level in ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
level = logging.getLevelName(conf_log_level)
logger.setLevel(level)
