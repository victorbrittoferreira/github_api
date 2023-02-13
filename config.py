import os
from os.path import dirname, join
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class UserGithubDossierConfig:
    URL_USER = (
        os.environ.get("URL_USER")
        or "https://api.github.com/users/{user_name}"
    )
    URL_USER_REPO = (
        os.environ.get("URL_USER_REPO")
        or "https://api.github.com/users/{user_name}/repos"
    )
    USER_NAME = os.environ.get("USER_NAME")
