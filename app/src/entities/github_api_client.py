import logging

import requests
from requests.exceptions import HTTPError

from src.entities.user_github import Repositories, UserBasicData

logger = logging.getLogger(__name__)


class GitHubClient:
    """
    Uses requests lib to access data from a given user by GitHub API.
    This class has methods to catch basic data and a list of repositories
    from the user.

    Attributes
    ----------
        - _BASE_URL : str
            GitHub base api url

        - user_name: str
            User`s name

    Methods
    -------
        - get_repositories_list : List | HTTPError

        - get_user_data : Dict | HTTPError

    """

    __slots__ = ("user_name",)

    _BASE_URL = "https://api.github.com/users"

    def __init__(self, user_name: str) -> None:
        self.user_name = user_name

    @property
    def user_url(self) -> str:
        return f"{self._BASE_URL}/{self.user_name}"

    def get_repositories_list(self) -> Repositories | HTTPError:
        """
        This returns the user's repositories list.

        Returns:
        --------
            - Repositories: If the request was successful, this returns
            a list of users repositories

        Example:
        --------
            >>> github_client = GitHubClient('victorbrittoferreira')
            >>> github_client.get_repositories_list()
            [{'id': 486252178, 'node_id': 'R_kgDOHPuekg', 'name': 'angular_todo_list',
              'full_name': 'victorbrittoferreira..._todo_list', ...}]

        Raises:
        ------
            - HTTPError:
                Raises when an HTTP error occur in the server or client side.
        """
        url = f"{self._BASE_URL}/{self.user_name}/repos"
        try:
            attempts = 3
            for _ in range(attempts):
                response = requests.get(url)
                if response.status_code == 200:
                    return response.json()
                response.raise_for_status()
        except HTTPError as error:
            logger.exception(
                "request_failed",
                extra={
                    "response_error_message": str(error),
                    "url": url,
                },
            )
            raise

    def get_user_data(self) -> UserBasicData | HTTPError:
        """
        This returns the user's basic personal profile info.

        Returns:
        --------
            - UserBasicData: If the request was successful, this returns
            a cict of basic profile info,like: name, url, public_repositories,
            followers, following.


        Example:
        --------
            >>> github_client = GitHubClient('victorbrittoferreira')
            >>> github_client.get_user_data()
            {login': 'victorbrittoferreira', 'id': 34899711,
             'node_id': 'MDQ6VXNlcjM0ODk5NzEx', ...}

        Raises:
        ------
            - HTTPError:
                Raises when an HTTP error occur in the server or client side.
        """
        try:
            attempts = 3
            for _ in range(attempts):
                response = requests.get(self.user_url)
                if response.status_code == 200:
                    return response.json()
                response.raise_for_status()
        except HTTPError as error:
            logger.exception(
                "request_failed",
                extra={
                    "response_error_message": str(error),
                    "url": self.user_url,
                },
            )
            raise

    def __str__(self) -> str:
        return f"""
        GitHub Client:
            Client name: {self.user_name}
        """

    def __repr__(self) -> str:
        return f"GitHubClient(name={self.user_name})"
