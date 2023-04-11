from config import ConfigApp
from src.main import extract_github_user_profile

if __name__ == "__main__":
    user_name = ConfigApp.GITHUB_USER_NAME
    github_personal_access_token = ConfigApp.GITHUB_PERSONAL_ACCESS_TOKEN
    extract_github_user_profile(user_name, github_personal_access_token)
