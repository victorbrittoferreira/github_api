import pytest
from requests.exceptions import HTTPError

from src.entities.github_api_client import GitHubClient
from tests.conftest import invalid_basic_types


# -------------------- GitHubClient.get_repositories_list()) --------------------------------
def test_get_repositories_list_returns_list(valid_username):
    # Test that the method valid data structure
    github_client = GitHubClient(valid_username)
    user_data = github_client.get_repositories_list()
    assert isinstance(user_data, list)
    assert isinstance(user_data[0], dict)


def test_expected_return_get_repositories_list(
    valid_username, valid_input_write_github_user_file
):
    # Test that the method return correct username repositories
    user = GitHubClient(valid_username)

    user_repositories_list = user.get_repositories_list()
    username = user_repositories_list[0]["full_name"].split("/")[0]
    repository_name = user_repositories_list[0]["name"]

    assert username == valid_username
    assert (
        repository_name
        in valid_input_write_github_user_file["repositories_name_list"]
    )


@pytest.mark.parametrize("invalid_basic_type", invalid_basic_types[3:-1])
def test_raises_exception_get_repositories_list(invalid_basic_type):
    # Test that the method raises an HTTPError exception if the input data is invalid
    user = GitHubClient(invalid_basic_type)

    with pytest.raises(HTTPError):
        user.get_repositories_list()


# -------------------- GitHubClient.get_user_data() --------------------------------
def test_get_user_data_returns_dict(valid_username):
    # Test that the method valid data structure
    github_client = GitHubClient(valid_username)
    user_data = github_client.get_user_data()
    assert isinstance(user_data, dict)


def test_expected_return_get_user_data(valid_username, valid_username_id):
    # Test that the method return correct username basic profile data
    user = GitHubClient(valid_username)

    user_repositories_list = user.get_user_data()
    assert user_repositories_list["id"] == valid_username_id


@pytest.mark.parametrize("invalid_basic_type", invalid_basic_types[3:-1])
def test_raises_exception_get_user_data(invalid_basic_type):
    # Test that the method raises an HTTPError exception if the input data is invalid
    user = GitHubClient(invalid_basic_type)
    with pytest.raises(HTTPError):
        user.get_user_data()
