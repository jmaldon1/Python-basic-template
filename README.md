# Python Basic Template

Basic template for starting python projects quickly

# Table of Contents
- [Python Basic Template](#python-basic-template)
- [Table of Contents](#table-of-contents)
- [How to set up](#how-to-set-up)
- [How to run](#how-to-run)
- [Tests](#tests)

# How to set up

1. Install requirements.

    ```shell
    $ pip install -r requirements.txt
    ```

2. Create a `.env` file.

    This file will hold all of your environment variables such as your passwords or any other sensitive information. Example `.env` file:

    ```shell
    export JOB_CONFIG=conf.dev_config
    export DB_PASS=pass123
    ```

3. Export `.env` variables (Skip if you installed the requirements).

    If you installed the requirements for this template, [python-dotenv](https://github.com/theskumar/python-dotenv) will export any environment variables for you and this step will be done automatically when you run the script.

    If you do not have `python-dotenv`, you can just run the following to manually export the variables:

    ```shell
    $ source .env
    ```

# How to run

```shell
$ python app.py
```

# Tests

Tests are in the `tests` directory

Run tests with:

```shell
$ pytest tests -v -s
```