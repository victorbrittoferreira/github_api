import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class ConfigApp:
    """
    Import configs
    """

    GITHUB_USER_NAME = os.environ.get("GITHUB_USER_NAME")

    def __str__(self) -> str:
        return f"""
        Config App:
            Client user_name: {self.GITHUB_USER_NAME}
        """

    def __repr__(self) -> str:
        return f"ConfigApp(user_name={self.GITHUB_USER_NAME})"
