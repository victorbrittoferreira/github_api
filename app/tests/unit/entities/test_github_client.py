# from requests.exceptions import HTTPError

from dataclasses import is_dataclass

from src.entities.github_api_client import GitHubClient
from src.schemas.git_profile import UserBasicData, UserRepositories


# -------------------- GitHubClient.get_repositories_list()) ------------------------
def test_get_repositories_list_returns_list(
    valid_username, github_personal_access_token_
):
    # Test that the method valid data structure
    github_client = GitHubClient(valid_username, github_personal_access_token_)
    user_data = github_client.get_repositories_list()
    # assert isinstance(user_data, UserRepositories)
    assert is_dataclass(user_data)


def test_expected_return_get_repositories_list(
    valid_username, github_personal_access_token_, repositories
):
    # Test that the method return correct username repositories
    github_client = GitHubClient(valid_username, github_personal_access_token_)

    user_repositories_list = github_client.get_repositories_list()
    username = (
        user_repositories_list.repositories[0]
        .repository["full_name"]
        .split("/")[0]
    )

    repository_name = user_repositories_list.repositories[0].repository["name"]

    assert username == valid_username

    any(repository_name in i.values() for i in repositories[0])


# -------------------- GitHubClient.get_user_data() --------------------------------


def test_get_user_data_returns_dict(
    valid_username, github_personal_access_token_
):
    # Test that the method valid data structure
    github_client = GitHubClient(valid_username, github_personal_access_token_)
    user_data = github_client.get_user_basic_data()
    # assert isinstance(user_data, UserBasicData)
    assert is_dataclass(user_data)


def test_expected_return_get_user_data(
    valid_username, github_personal_access_token_, valid_username_id
):
    # Test that the method return correct username basic profile data
    github_client = GitHubClient(valid_username, github_personal_access_token_)

    user_data = github_client.get_user_basic_data()
    assert user_data.user_basic_data["id"] == valid_username_id
