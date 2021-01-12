"""Development configuration file.
"""
DESCRIPTION = "Description of app."
ENVIRONMENT = "DEV"

config = {
    "name": __name__,
    "description": DESCRIPTION,
    "environment": ENVIRONMENT,
    # Log level options: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
    "log_level": "INFO",
    "api": {
        "host": "localhost",
        "port": 5000,
        "debug": True,
    },
    "database": {
        "host": "http://0.0.0.0:3000",
    }
}
