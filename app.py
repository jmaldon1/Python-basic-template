"""Entry point of the project
"""
import json

import settings as _  # Loader script for initializing things.
from conf import config
from src.logger import logger


def main():
    """Main function
    Run this file with `python app.py`
    """
    print("\n")
    logger.info("Success! Here is you're config:\n")
    logger.info(json.dumps(config, indent=4))


if __name__ == "__main__":
    main()
