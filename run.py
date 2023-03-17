from config import ConfigApp
from src.main import pursuit_profile


if __name__ == "__main__":
    user_name = ConfigApp.GITHUB_USER_NAME or input("Insert the user name:\n")
    pursuit_profile(user_name)
