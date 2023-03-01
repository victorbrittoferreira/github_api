from src.entities.github_api_client import GitHubClient
from test.conftest import invalid_basic_types
import pytest

from requests.exceptions import HTTPError


@pytest.mark.parametrize("invalid_basic_type", invalid_basic_types[3:-1])
def test_raises_get_repositories_list(invalid_basic_type):
    user = GitHubClient(invalid_basic_type)

    with pytest.raises(HTTPError):
        user.get_repositories_list()


@pytest.mark.parametrize("invalid_basic_type", invalid_basic_types[3:-1])
def test_raises_get_user_data(invalid_basic_type):
    user = GitHubClient(invalid_basic_type)
    with pytest.raises(HTTPError):
        user.get_user_data()
