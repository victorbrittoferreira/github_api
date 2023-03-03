from config import GITHUB_USER_NAME
from src.main import pursuit_profile


if __name__ == "__main__":
    user_name = GITHUB_USER_NAME or input("Insert the user name:\n")
    pursuit_profile(user_name)
