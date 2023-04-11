import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class ConfigApp:
    """
    A class to manage configuration settings for your application.

    This class loads configuration settings from environment variables defined in a .env file.
    To use this class, you should define all required environment variables in your .env file
    and instantiate the class in your application code.

    Usage:
        1. Define required environment variables in a .env file in the root of your project.
           For example:
               GITHUB_USER_NAME=myusername
        2. Instantiate the ConfigApp class in your application code:
               config = ConfigApp()
        3. Access configuration settings using the properties of the ConfigApp object:
               print(config.GITHUB_USER_NAME)

    Note:
        - All required environment variables should be defined as fields of this class.
        - If a required environment variable is not defined in the .env file, a KeyError will be raised.
        - Avoid use .get() method or use some check statment for that.
    """

    GITHUB_USER_NAME = os.environ["GITHUB_USER_NAME"]
    GITHUB_PERSONAL_ACCESS_TOKEN = os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"]
