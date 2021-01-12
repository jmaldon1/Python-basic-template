"""Finds location of config file from environment variables
"""
import os
from importlib import import_module

from src.logger import logger

try:
    config_module = import_module(os.environ['JOB_CONFIG'])
    # This pulls `config` dictionary from appropriate module
    config = config_module.config
    logger.info("Found config.")
except KeyError as err:
    logger.error("Can't find environment variable %s", err)
    raise
